from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    fathers_name=models.CharField(max_length=100,default='')
    course=models.CharField(max_length=20,default='')
    technology=models.CharField(max_length=40,default='')
    role=models.CharField(max_length=20,default=0)

    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)



