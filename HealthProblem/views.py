from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from about.forms import DoctorForm
from doctor.models import doctor
from Account.models import UserProfile

def index( request):
    if 
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
