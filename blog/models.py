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
        word_array = self.body.split()

        summary_text = ''
        iteration = 0
        for word in word_array:
            if iteration > 30:
                break
            summary_text += word + ' '
            iteration += 1

        return summary_text + '(...)'

    def pub_date_cleaned(self):
        return self.pub_date.strftime('%b %e, %Y')

    def formatted_body(self):
        paragraph_array = self.body.split('  ')

        body_text = ""

        for paragraph in paragraph_array:
            body_text += paragraph + '\n\n'

        return body_text
