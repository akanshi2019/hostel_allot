from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from hostel.models import User


class allot(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.your_name

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        allot.objects.create(user=instance)