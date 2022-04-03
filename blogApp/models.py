from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


# this model will hold the tags of each posts
class Tag(models.Model):
    tag_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.tag_name


# this model will hold the posts
class Article(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=False)
    body = tinymce_models.HTMLField(blank=False)
    image_url = models.URLField(max_length=2000, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
