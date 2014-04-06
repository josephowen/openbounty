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
    doers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='proofs', through='Proof')

    
class BountyUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    wallet = models.DecimalField(default=0,decimal_places=2,max_digits=500)
    access_token = models.CharField(max_length = 100, blank=True, default=None)
    venmo = models.CharField(max_length = 60, blank=True, default="")

class Backing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    challenge = models.ForeignKey(Challenge)

class Proof(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    challenge = models.ForeignKey(Challenge)
    url = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=5000)
    votes = models.IntegerField(default=0)
    winner = models.BooleanField(default=False)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="claim_votes", through='ClaimVotes')

class ClaimVotes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    claim = models.ForeignKey(Proof)
