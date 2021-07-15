from django.db import models

# Create your models here.


class MessageTopic(models.Model):

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'messages'

    def __str__(self):
        return f"{self.text[:50]}..."










