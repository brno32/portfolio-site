from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=160)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.CharField(max_length=1600)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_cleaned(self):
        return self.pub_date.strftime('%b %e, %Y')
