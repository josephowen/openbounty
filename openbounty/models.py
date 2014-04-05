from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.conf import settings

'''
class MyUserManager(BaseUserManager):
    def create_user(self, identifier, phone_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not identifier:
            raise ValueError('Users must have an email address')

        user = self.model(
            identifier=identifier,
	    phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identifier, phone_number, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            identifier=identifier,
	    phone_number = phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class BountyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True, db_index=True)
    USERNAME_FIELD = 'identifier'
    phone_number = models.CharField(max_length=15)
    REQUIRED_FIELDS = ['phone_number']
    
    objects = MyUserManager()
    
    def get_full_name():
        return USERNAME_FIELD
    
    def get_short_name():
        return USERNAME_FIELD
'''

# Create your models here.
class Challenge(models.Model):
    bounty = models.FloatField()
    title = models.CharField(max_length = 120)
    challenge = models.CharField(max_length = 2000)
    expiration_date = models.DateTimeField("Challenge Expiration Date")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    backers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='backings', through='Backing')

    
class BountyUser(AbstractUser):
    phone_number = models.CharField(max_length=15)


class Backing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    challenge = models.ForeignKey(Challenge)
    
