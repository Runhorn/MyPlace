from django.db import models
from datetime import datetime


class Owner(models.Model):
    name_and_surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='media/%Y/%m/%d')
    email = models.CharField(max_length=30)
    joined = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name_and_surname
