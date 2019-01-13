from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Account.models import UserProfile
# Create your models here.
class medical(models.Model):
    Male='M'
    Female='F'
    sex=((Male,'male'),
    (Female,'female'),
    )

    phoneno=models.IntegerField(default=0)
    temporary_address=models.CharField(max_length=30)
    permanent_address=models.CharField(max_length=30)
    sex=models.CharField(max_length=2,choices=sex,default='M')
    age=models.IntegerField(default=0)
    post=models.CharField(max_length=30)
    image=models.FileField(upload_to='profilepicture')
    Portfolio = models.URLField(default=0)
    join_date=models.DateField(timezone.now(),null=True)
    user=models.OneToOneField(UserProfile,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
