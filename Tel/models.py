from django.conf import settings
from django.db import models
from django.utils import timezone


class Tel(models.Model):
    FIO = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

 