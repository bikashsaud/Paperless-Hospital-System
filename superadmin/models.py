from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Account.models import UserProfile
# Create your models here.

class superadmin(models.Model):
    Male='M'
    Female='F'
    sex=(
        (Male,'male'),
        (Female,'female'),
        )
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    phoneno=models.IntegerField(default=0,blank=True,null=True)
    p_address=models.CharField(max_length=300,default=0,blank=True,null=True)
    t_address=models.CharField(max_length=300,default=0)
    sex=models.CharField(max_length=2,choices=sex,default='M')
    age=models.IntegerField(default=0)
    post=models.CharField(max_length=30,default=0)
    image=models.FileField(upload_to='profilepicture',blank=True)
    cv=models.FileField(upload_to='cv/')
    Portfolio = models.URLField(default=0)
    degree=models.CharField(max_length=250,default=0)
    university=models.CharField(max_length=100,default=0)
    experience=models.IntegerField(default=0)
    join_date=models.DateField(timezone.now(),blank=True,null=True)

    def __str__(self):
        return self.user.name
