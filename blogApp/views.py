from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Article


# Create your views here.
def home(request):
    all_blog_items = Article.objects.all().order_by('-timestamp')
    author_name = User.get_full_name
    context = {
        'items': all_blog_items,
        'author_name': author_name,
    }
    return render(request, 'blogApp/home.html', context)


def about(request):
    return render(request, 'blogApp/about.html', {})


def blogs(request):
    return render(request, 'blogApp/blogs.html', {})
