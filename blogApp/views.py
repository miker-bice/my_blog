from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Article


# Create your views here.
def home(request):
    all_blog_items = Article.objects.filter(active=True, featured=True).order_by('-timestamp')
    author_name = User.get_full_name
    context = {
        'items': all_blog_items,
        'author_name': author_name,
    }
    return render(request, 'blogApp/home.html', context)


def about(request):
    return render(request, 'blogApp/about.html', {})


def blogs(request):
    # this is for the latest blogs
    latest_blog = Article.objects.last()

    # this is for all the active blogs published
    all_items = Article.objects.filter(active=True).order_by('-timestamp')[1:]

    context = {
        'latest_item': latest_blog,
        'items': all_items,
    }
    return render(request, 'blogApp/blogs.html', context)


def blog(request, blog_id):
    item = get_object_or_404(Article, pk=blog_id)
    context = {
        'item': item
    }
    return render(request, 'blogApp/blog.html', context)
