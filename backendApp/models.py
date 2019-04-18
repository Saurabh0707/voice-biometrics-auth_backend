from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self, email, voiceit_id, password):
        if not email:
            raise ValueError('Email is required')
        if not voiceit_id:
            raise ValueError('Sorry, Error with your voiceprint')
        email = self.normalize_email(email)
        user = self.model(email = email, voiceit_id = voiceit_id)
        user.set_password(password)

        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password, voiceit_id):
        user = self.create_user(email, voiceit_id, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True, max_length = 255)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default= True)
    voiceit_id = models.CharField(max_length= 255)
    is_staff  = models.BooleanField(default= False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['voiceit_id']

    def __str__(self):
        return self.email
