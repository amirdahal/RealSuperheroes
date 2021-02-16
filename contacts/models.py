from django.db import models
from django.shortcuts import reverse

class Message(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=30)
    Message = models.TextField()
    Read = models.BooleanField(default=False)

    def __str__(self):
        return self.Subject

    def get_absolute_url(self):
        return reverse('contact', kwargs={})
    
