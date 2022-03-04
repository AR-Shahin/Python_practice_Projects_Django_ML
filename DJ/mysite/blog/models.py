
from distutils.command import upload
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, default="Default Post")
    slug = models.SlugField(max_length=200, default="Default-Post")
    image = models.ImageField(null=True, upload_to="media")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
