from django.db.models.signals import post_save
from django.dispatch import receiver
from News.models import Interview

@receiver(post_save, sender=Interview)
def transcript(sender, instance, created, **kwargs):
    if created:
        print('post save')
        vid_url = instance.video.url
        print(vid_url)
        _id = instance.id
        command = "ffmpeg -i {} -vn -ar 44100 -ac 1 -b:a 32k -f mp3 media/temp/audio/{}.mp3".format(vid_url, _id)
        os.system(command)
        
        audio_file = "media/temp/audio/{}.mp3".format(_id)

        with open(audio_file, mode="rb") as file:
            post_body = file.read()

        # configure api
        secret_key = "fa64ad2cfb2041a89807375880802697"
        endpoint = "https://api.speechtext.ai/recognize?"
        header = {'Content-Type': "application/octet-stream"}


        config = {
            "key" : secret_key,
            "language" : "en-US",
            "punctuation" : True,
            "format" : "mp3"
        }

        r = requests.post(endpoint, headers = header, params = config, data = post_body).json()
        task = r["id"]

        config = {
            "key" : secret_key,
            "task" : task,
            "summary" : True,
            "output" : "vtt",
            "highlights" : True,
            "max_caption_words" : 15
        }

        subtitles = get_results(config)
        subtitle_file = "media/temp/subtitles/{}.vtt".format(_id)
        with open(subtitle_file, 'w') as f:
            print(subtitles, file=f)

        setattr(instance, subtitles, subtitle_file)
        instance.save()


def get_results(config):
    endpoint = "https://api.speechtext.ai/results?"
    while True:
        results = requests.get(endpoint, params=config).json()
        if "status" not in results:
            break
        print("Task status: {}".format(results["status"]))
        if results["status"] == 'failed':
            print("The task is failed: {}".format(results))
            break
        if results["status"] == 'finished':
            break
        time.sleep(15)
    return results