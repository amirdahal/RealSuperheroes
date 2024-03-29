from django.shortcuts import render
from .models import News, Category, Interview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    news_obj = News.objects.all().order_by("-id")[:10]
    int_obj = Interview.objects.all().order_by("-id")[:8]
    context = {
        'news':news_obj,
        'interview': int_obj
    }
    return render(request, 'News/home.html', context)

class PostDetailView(DetailView):
    model = News
    template_name = 'News/single_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['allnews'] = News.objects.all()
        return context

# Create your views here.
def AllNews(request):
    news_obj = News.objects.all().order_by("-id")
    context = {
        'news':news_obj,
        'category': 'All News'
    }
    return render(request, 'News/all_news.html', context)


def CategoryNews(request, pk):
    news_obj = News.objects.filter(category_id = pk).order_by("-id")
    context = {
        'news': news_obj,
        'category': news_obj.last().category
    }
    return render(request, 'News/all_news.html', context)
