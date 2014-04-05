from django.contrib.auth import models.AbstractBaseUser
from django.db import models
from django.conf import settings


# Create your models here.
class Challenge(models.Model):
    bounty = models.FloatField()
    title = models.CharField(max_length = 120)
    challenge = models.CharField(max_length = 2000)
    expiration_date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    
class BountyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True, db_index=True)
    USERNAME_FIELD = 'identifier'
    phone_number = models.CharField()
    REQUIRED_FIELDS = ['phone_number']
    
    def get_full_name():
        return USERNAME_FIELD
    
    def get_short_name():
        return USERNAME_FIELD
    
