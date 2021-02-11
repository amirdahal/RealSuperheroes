from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from ckeditor.fields import RichTextField
from django.shortcuts import reverse

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_interview', kwargs={'pk': self.pk})
    

