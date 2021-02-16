from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from ckeditor.fields import RichTextField
from django.shortcuts import reverse

# test imports
import os
import requests
import time
import json

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=250)
    image = models.ImageField(default='default.jpg', upload_to='news_images')
    summary = models.TextField()
    text = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('single_news', kwargs={'pk': self.pk})

class Interview(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    thumbnail = models.ImageField(default='interview/thumbnail/default.jpg',upload_to='interviews/thumbnail')
    video = models.FileField(upload_to='interviews')
    event_date = models.DateField()
    date_posted = models.DateTimeField(default=timezone.now)
    subtitles = models.FileField(upload_to='interviews/subtitles', blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_interview', kwargs={'pk': self.pk})

    # test code
    def post_save(self):
        vid_url = self.video.url
        _id = self.id
        command = "ffmpeg -i {} -vn -ar 44100 -ac 1 -b:a 32k -f mp3 /media/interviews/audio/{}.mp3".format(vid_url, _id)
        os.system(command)

        audio_file = "/media/interviews/audio/{}.mp3".format(_id)

        with open(audio_file, mode="rb") as file:
            post_body = file.read()

        # endpoint to start a transcription task
        endpoint = "https://api.speechtext.ai/recognize?"
        header = {'Content-Type': "application/octet-stream"}
        secret_key = "fa64ad2cfb2041a89807375880802697"
        r = requests.post(endpoint, headers = header, params = config, data = post_body).json()
        task = r["id"]
        config = {
            "key" : secret_key,
            "task" : task,
            "output" : "vtt",
            "max_caption_words" : 15
        }
        
        # endpoint to check status of the transcription task
        endpoint = "https://api.speechtext.ai/results?"
        # use a loop to check if the task is finished
        results = ""
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
            # sleep for 15 seconds if the task has the status - 'processing'
            time.sleep(15)
        #print("Subtitles: {}".format(subtitles))
        subtitle_file = "{}.vtt".format(_id)
        with open(subtitle_file, 'w') as f:
            print(results, file=f)
        self.subtitles = subtitle_file

