from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin

class ContactUs(CreateView):
    model = Message
    fields = ['Name', 'Email', 'Subject', 'Message']
    template_name = "contacts/contactus.html"

class Messages(LoginRequiredMixin, ListView):
    model = Message
    template_name = "contacts/messages.html"
    context_object_name = "messages"