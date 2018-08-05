from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from hostel.models import UserProfile


class allot(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=UserProfile)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        allot.objects.create(user=instance)