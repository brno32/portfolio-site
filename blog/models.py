from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=160)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.CharField(max_length=1600)
    image = models.ImageField(upload_to='images/')
