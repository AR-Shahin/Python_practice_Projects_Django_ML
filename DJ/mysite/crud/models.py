
from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
