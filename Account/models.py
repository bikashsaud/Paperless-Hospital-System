from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# from django.utils import timezone

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("user must require email address")
        email=self.normalize_email(email)
        user=self.model(
            email=email,
            name=name
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staff(self,email,name,password=None):
    #     user=self.create_user(password,name,email)
    #     user.is_superuser=False,
    #     user.is_staff=True
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password=password)
        user.is_admin=False
        user.is_staff=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email=models.EmailField(max_length=150,unique=True)
    name=models.CharField(max_length=150)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_doctor=models.BooleanField(default=False)
    is_medical=models.BooleanField(default=False)
    is_lab=models.BooleanField(default=False)
    # is_patient=models.BooleanField(default=True)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.email
    def get_short_name(self):
        return self.email
    def get_full_name(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
