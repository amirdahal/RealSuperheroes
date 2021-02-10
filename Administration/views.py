from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from News.models import News
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def logout_view(request):
    logout(request)
    messages.success(request, f'You have been logged out!!!')
    return redirect('login')

def manage(request):
    news_obj = News.objects.all()
    context = {
        'news': news_obj
    }
    return render(request, 'Administration/manage.html', context)


class AddNews(LoginRequiredMixin, CreateView):
    model = News
    fields = ['category','headline', 'image', 'summary', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditNews(LoginRequiredMixin, UpdateView):
    model = News
    fields = ['category','headline', 'image', 'summary', 'text']

@login_required
def DeleteNews(request, pk): 
    obj = get_object_or_404(News, id = pk) 
    if request.method =="POST":  
        obj.delete()
        messages.success(request, f'News has been deleted!')
        return redirect('/manage/')
    return render(request, "Administration/delete_news.html") 
