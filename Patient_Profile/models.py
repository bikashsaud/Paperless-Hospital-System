from django.db import models
from django.utils import timezone
from Account.models import UserProfile
from staff.models import Staff
from doctor.models import doctor
from lab.models import lab
from medical.models import medical
# from ckeditor.fields import RichTextField
# Create your models here.
class Patient(models.Model):
    """docstring for Patient."""
    Male='M'
    Female='F'
    sex=((Male,'male'),
    (Female,'female'),
    )
    user=models.ForeignKey(Staff)
    name=models.CharField(max_length=50,default='saud')
    email=models.EmailField(max_length=150,default='saud@gmail.com')
    sex=models.CharField(max_length=2,choices=sex,default='M')
    age=models.IntegerField(default=0)
    date=models.DateField(timezone.now(),null=True)
    address=models.CharField(max_length=30,default='0')
    phoneno=models.IntegerField(default=0)
    about=models.TextField(default='0')

    def __str__(self):
        return self.name
class D_Medical(models.Model):
    medicine_name=models.TextField(default='0')
    comment=models.TextField(default='0')
    follow_on_date=models.DateField(timezone.now(),null=True)
    date=models.DateTimeField(timezone.now(),blank=False)
    is_purchased=models.BooleanField(default=False,)
    amount=models.IntegerField(default=0.0)
    patient=models.ForeignKey(Patient)
    doctor=models.ForeignKey(doctor)

    def __str__(self):
        return self.patient.name

class D_Lab(models.Model):
    test_list=models.TextField(default='0')
    comment=models.TextField(default='0')
    is_sampled=models.BooleanField(default=False)
    result=models.CharField(max_length=100,default='Pending')
    doctor=models.ForeignKey(doctor)
    patient=models.ForeignKey(Patient)

    def __str__(self):
        return self.patient.name

class Test_result(models.Model):
    test_name=models.CharField(max_length=200,default='0')

    test_date=models.DateField(timezone.now(),null=True,blank=True)

    lab=models.ForeignKey(lab)
    patient=models.ForeignKey(Patient)
    doctor=models.ForeignKey(doctor)

    def __str__(self):
        return self.patient.name

class Medicine(models.Model):
    medicine_name=models.TextField(default='0')
    test_date=models.DateField(timezone.now())
    amount=models.IntegerField(default='0')
    doctor=models.ForeignKey(doctor)
    patient=models.ForeignKey(Patient)
    medical=models.ForeignKey(medical)

    def __str__(self):
        return self.patient.name
