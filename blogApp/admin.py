from django.contrib import admin
from .models import Tag, Article


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'title', 'featured', 'active', 'timestamp')


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
