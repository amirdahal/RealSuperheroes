from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from News.models import Interview

class InterviewDetailView(DetailView):
    model = Interview
    template_name = 'Interview/single_interview.html'
    context_object_name = 'interview'


def AllInterview(request):
    int_obj = Interview.objects.all()
    context = {
        'interview': int_obj
    }
    return render(request, 'Interview/all_interview.html', context)