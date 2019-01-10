from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Account.models import UserProfile
# Create your models here.
class Staff(models.Model):

    Male='M'
    Female='F'
    sex=((Male,'male'),
    (Female,'female'),
    )
    SLC='S'
    Intermediate='I'
    Bachelor='B'
    Master='M'
    AboveMaster='A'
    degree=((SLC,'SLC'),(Intermediate,'Intermediate'),(Master,'Bachelor'),(Master,'Master'),(AboveMaster,'AboveMaster'),)
    # date_choices=[x for x in renge(1975,2018)]
    phoneno=models.IntegerField(default=0)
    address=models.CharField(max_length=30)
    sex=models.CharField(max_length=2,choices=sex,default='M')
    age=models.IntegerField(default=0)
    post=models.CharField(max_length=30)
    image=models.FileField(upload_to='profilepicture')
    cv=models.FileField(upload_to='cv/')
    Portfolio = models.URLField()
    degree=models.CharField(max_length=2,choices=degree,default='S')
    #join_date=models.DateField(initial=TIME_ZONE.now(),widget=form.SelectDateWidget(date_choices=date_choices))
    join_date=models.DateField(timezone.now(),null=True)
    user=models.OneToOneField(UserProfile,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
