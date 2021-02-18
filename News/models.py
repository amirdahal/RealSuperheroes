from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
import math


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

    def whenpublished(self):
        now = timezone.now()
        diff= now - self.date_posted

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "sec ago"
            else:
                return str(seconds) + " secs ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " min ago"
            else:
                return str(minutes) + " mins ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"
        
        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"


class Interview(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    thumbnail = models.ImageField(default='interview/thumbnail/default.jpg',upload_to='interviews/thumbnail')
    video = models.FileField(upload_to='interviews')
    event_date = models.DateField()
    date_posted = models.DateTimeField(default=timezone.now)
    subtitles = models.FileField(upload_to='interviews/subtitles', blank=True)
    transcript = models.TextField(default="Data unavailable!")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_interview', kwargs={'pk': self.pk})