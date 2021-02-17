from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from News.models import News, Interview
from .forms import AddInterviewForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import reverse

from Administration import transcribe


def logout_view(request):
    logout(request)
    messages.success(request, f'You have been logged out!!!')
    return redirect('login')

@login_required
def manage_news(request):
    news_obj = News.objects.all()
    context = {
        'news': news_obj
    }
    return render(request, 'Administration/manage_news.html', context)

@login_required
def manage_interviews(request):
    interview_obj = Interview.objects.all()
    context = {
        'news': interview_obj
    }
    return render(request, 'Administration/manage_interviews.html', context)


class AddNews(LoginRequiredMixin, CreateView):
    model = News
    fields = ['category','headline', 'image', 'summary', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class AddInterview(LoginRequiredMixin, CreateView):
#     model = Interview
#     fields = ['title', 'thumbnail','event_date', 'description', 'video']


@login_required
def AddInterview(request):
    if request.method == 'POST':
        form = AddInterviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Added!')
            interview_obj = Interview.objects.all().last()
            transcribe.run(interview_obj)
            return redirect(reverse('single_interview', kwargs={'pk': interview_obj.id}))
    else:
        form = AddInterviewForm()
    return render(request, 'Administration/add_interview.html', {'form': form})
    

class EditNews(LoginRequiredMixin, UpdateView):
    model = News
    fields = ['category','headline', 'image', 'summary', 'text']

class EditInterview(LoginRequiredMixin, UpdateView):
    model = Interview
    fields = ['title', 'thumbnail','event_date', 'description', 'video']


@login_required
def DeleteNews(request, pk): 
    obj = get_object_or_404(News, id = pk) 
    if request.method =="POST":  
        obj.delete()
        messages.success(request, f'News has been deleted!')
        return redirect('manage_news')
    return render(request, "Administration/delete_news.html") 


@login_required
def DeleteInterview(request, pk): 
    obj = get_object_or_404(Interview, id = pk) 
    if request.method =="POST":  
        obj.delete()
        messages.success(request, f'Interview has been deleted!')
        return redirect('manage_interview')
    return render(request, "Administration/delete_interview.html") 
