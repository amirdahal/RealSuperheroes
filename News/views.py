from django.shortcuts import render
from .models import News, Category, Interview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
def home(request):
    news_obj = News.objects.all()[:4]
    int_obj = Interview.objects.all()[:2]
    context = {
        'news':news_obj,
        'interview': int_obj
    }
    return render(request, 'News/home.html', context)

class PostDetailView(DetailView):
    model = News
    template_name = 'News/single_news.html'
    context_object_name = 'news'

# Create your views here.
def AllNews(request):
    news_obj = News.objects.all()
    context = {
        'news':news_obj,
        'category': 'All News'
    }
    return render(request, 'News/all_news.html', context)


def CategoryNews(request, pk):
    news_obj = News.objects.filter(category_id = pk)
    #cat = Category.objects.filter(id=pk)
    #cat = Category.objects.get(category = pk)
    context = {
        'news': news_obj,
        # 'category': cat
    }
    return render(request, 'News/all_news.html', context)

# def CategoryNews(request, pk): 
#     obj = get_object_or_404(News, category = pk) 
#     return render(request, "Administration/delete_news.html") 

# class AllNews(ListView):
#     model = News
#     news_obj = News.objects.all()
#     template_name = 'News/all_news.html'
#     context_object = {
#         'category': 'All News',
#         'news': news_obj
#     }