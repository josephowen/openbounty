from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.conf import settings

# Create your models here.
class Challenge(models.Model):
    bounty = models.FloatField()
    title = models.CharField(max_length = 120)
    challenge = models.CharField(max_length = 2000)
    post_date = models.DateTimeField("Post Date")
    expiration_date = models.DateTimeField("Challenge Expiration Date")
    fulfilled = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    backers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='backings', through='Backing')

    
class BountyUser(AbstractUser):
    phone_number = models.CharField(max_length=15)


class Backing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    challenge = models.ForeignKey(Challenge)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    challenge = models.ForeignKey(Challenge)
    title = models.CharField(max_length = 120)
    comment = models.CharField(max_length = 2000)
    date_posted = models.DateTimeField("Date Posted")
    
