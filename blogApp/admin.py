from django.contrib import admin
from .models import Tag, Article


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('')