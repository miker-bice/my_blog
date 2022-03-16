from django.urls import path
from . import views

app_name = 'blogApp'

urlpatterns = [
    path('', views.home, name='home'),
]