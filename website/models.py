from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    published_on = models.DateTimeField('date published')
