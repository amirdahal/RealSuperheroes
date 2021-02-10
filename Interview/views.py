from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from News.models import Interview

class InterviewDetailView(DetailView):
    model = Interview
    template_name = 'Interview/single_interview.html'
    context_object_name = 'interview'
