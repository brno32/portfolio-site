from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    note = models.CharField(max_length=80, default='')
    github_link = models.CharField(max_length=100, default='')
    use_link = models.CharField(max_length=100, default='')
