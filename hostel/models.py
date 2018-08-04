from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    #choices = [
      #  ('applicant', 'Applicant'),
     #   ('executive', 'Executive'),
    #]
    user=models.OneToOneField(User)
    fathers_name=models.CharField(max_length=100,default='')
    course=models.CharField(max_length=20,default='')
    technology=models.CharField(max_length=40,default='')
    #choice=models.CharField(max_length=20,default=0)
@receiver(post_save,sender=User)
def create_proile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.created(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
   instance.profile.save()
    #if kwargs['created']:
    #    user_profile=UserProfile.objects.create(user=kwargs['instance'])
#post_save.connect(create_proile,sender=User)


