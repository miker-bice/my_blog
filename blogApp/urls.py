from django.urls import path
from . import views

app_name = 'blogApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
]