from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Challenge(models.Model):
    bounty = models.DecimalField(decimal_places=2,max_digits=500)
    title = models.CharField(max_length = 120)
    challenge = models.CharField(max_length = 2000)
    post_date = models.DateTimeField("Post Date", default=datetime.now)
    expiration_date = models.DateTimeField("Challenge Expiration Date")
    fulfilled = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    backers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='backings', through='Backing')

    
class BountyUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    wallet = models.DecimalField(default=0,decimal_places=2,max_digits=500)
    access_token = models.CharField(max_length = 100, blank=True, default=None)

class Backing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    challenge = models.ForeignKey(Challenge)
