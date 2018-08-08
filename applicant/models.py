from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Allot(models.Model):
    first_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.first_name
