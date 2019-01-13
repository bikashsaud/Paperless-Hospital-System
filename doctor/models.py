from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from Account.models import UserProfile
# from django.db.models.signals import post_save
# Create your models here.
class doctor(models.Model):
    Male='M'
    Female='F'
    sex=(
        (Male,'male'),
        (Female,'female'),
        )
    phoneno=models.IntegerField(default=0)
    p_address=models.CharField(max_length=300)
    t_address=models.CharField(max_length=300)
    sex=models.CharField(max_length=2,choices=sex,default='M')
    age=models.IntegerField(default=0)
    specialist=models.CharField(max_length=200,null=True)
    image=models.FileField(upload_to='profilepicture',null=True)
    cv=models.FileField(upload_to='cv/',null=True,blank=True)
    Portfolio = models.URLField(null=True,blank=True)
    degree=models.CharField(max_length=250)
    university=models.CharField(max_length=100)
    experience=models.IntegerField(default=0)
    join_date=models.DateField(timezone.now(),null=True)
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
