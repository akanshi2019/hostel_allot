from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    fathers_name=models.CharField(max_length=100,default='')
    course=models.CharField(max_length=20,default='')
    technology=models.CharField(max_length=40,default='')
    #choice=models.IntegerField(default=0)


def create_proile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_proile,sender=User)
