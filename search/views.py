from django.shortcuts import render
from News.models import News, Interview
from django.db.models import Q

def Search(request):
    if request.method == 'GET':
        query= request.GET.get('query')

        if query is not None:
            news_lookup = Q(headline__icontains=query) | Q(summary__icontains=query) | Q(text__icontains=query)
            news_result= News.objects.filter(news_lookup).distinct()

            interview_lookup = Q(title__icontains=query) | Q(description__icontains=query)
            interview_result = Interview.objects.filter(interview_lookup).distinct()

            context={
                'news_result': news_result,
                'interview_result': interview_result
            }
            return render(request, 'search/search.html', context)
    else:
        return render(request, 'search/search.html')

    return render(request, 'search/search.html')
