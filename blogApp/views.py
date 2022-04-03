from django.shortcuts import render
from .models import Article


# Create your views here.
def home(request):
    all_blog_items = Article.objects.all().order_by('timestamp')
    context = {
        'items': all_blog_items
    }
    return render(request, 'blogApp/home.html', context)


def about(request):
    return render(request, 'blogApp/about.html', {})


def blogs(request):
    return render(request, 'blogApp/blogs.html', {})
