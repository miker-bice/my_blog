from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'blogApp/home.html', {})


def about(request):
    return render(request, 'blogApp/about.html', {})


def blogs(request):
    return render(request, 'blogApp/blogs.html', {})
