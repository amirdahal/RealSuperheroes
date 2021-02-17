import os
import speech_recognition as sr 
import moviepy.editor as mp
from pprint import pprint
import requests
import time
import json



def run(current_obj):
	vid_url = current_obj.video.path
	_id = current_obj.id
	print('vid_url = ',vid_url) 
	clip = mp.VideoFileClip(vid_url)
	audio_filename = "media/temp/audio/{}.mp3".format(_id) 
	clip.audio.write_audiofile(audio_filename)

	with open(audio_filename, mode="rb") as file:
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

	# setattr(current_obj, subtitles, subtitle_file)
	# current_obj.save()

	current_obj.subtitles = "temp/subtitles/{}.vtt".format(_id)
	current_obj.save()

	# def form_valid(self, form):
 #        form.instance.author = self.request.user
 #        return super().form_valid(form)

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

