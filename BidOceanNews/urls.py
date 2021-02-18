from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from News import views as news_views
from News.views import PostDetailView, AllNews
from django.contrib.auth import views as auth_views
from Administration import views as admin_views
from Interview.views import InterviewDetailView, AllInterview
from contacts.views import ContactUs, Messages
from search.views import Search


urlpatterns = [
    #django-admin
    path('admin/', admin.site.urls),

    #home
    path('', news_views.home, name="home"),
    path('home/', news_views.home, name="home"),

    #contact, message & search
    path('contact/', ContactUs.as_view(), name="contact"),
    path('message/', Messages.as_view(), name="message"),
    path('search/', Search, name="search"),

    #news
    path('news/', news_views.AllNews, name="all_news"),
    path('news/add/', admin_views.AddNews.as_view(template_name='Administration/add_news.html'), name="add_news"),
    path('news/<int:pk>/', PostDetailView.as_view(), name="single_news"),
    path('news/category/<int:pk>',news_views.CategoryNews , name="category_news"),    
    path('manage/news/', admin_views.manage_news, name="manage_news"),
    path('news/<int:pk>/edit', admin_views.EditNews.as_view(template_name='Administration/edit_news.html'), name="edit_news"),
    path('news/<int:pk>/delete', admin_views.DeleteNews, name="delete_news"),

    #interviews
    path('interview/', AllInterview, name="all_interview"),
    path('interview/<int:pk>', InterviewDetailView.as_view(), name="single_interview"),
    path('interview/add/', admin_views.AddInterview, name="add_interview"),
    path('manage/interviews/', admin_views.manage_interviews, name="manage_interview"),
    path('interview/<int:pk>/edit', admin_views.EditInterview.as_view(template_name='Administration/edit_interview.html'), name="edit_interview"),
    path('interview/<int:pk>/delete', admin_views.DeleteInterview, name="delete_interview"),

    #admin login & logout
    path('login/', auth_views.LoginView.as_view(template_name = 'Administration/login.html'), name='login'),
    path('logout/', admin_views.logout_view, name='logout'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)