from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from . import views
# from django.apps import apps
from django.http import HttpResponse
from .forms import UserCreationForm,UserLoginForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import UserProfile

from doctor.models import doctor
from staff.models import Staff
from lab.models import lab
from medical.models import medical
from superadmin.models import superadmin

from about.forms import DoctorForm
from django.contrib import messages
User=get_user_model()


# Create your views here.
@login_required
def register(request,*args,**kwargs):
    if( request.user.is_admin) | (request.user.is_staff):
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            obj=UserProfile.objects.latest('id')
            if(form.cleaned_data.get('is_doctor')==True):
                doct=doctor(user=obj)
                doct.save()
            if request.POST.get('is_staff'):
                l=Staff(user=obj)
                l.save(obj)

            elif request.POST.get('is_medical'):
                l=medical(user=obj)
                l.save(obj)
            elif request.POST.get('is_lab'):
                l=lab(user=obj)
                l.save(obj)
            elif request.POST.get('is_admin'):
                l=superadmin(user=obj)
                l.save(obj)
            # else:
            #     pass
            # print(who)
            # print(obj)

            print("user Creted0")
            messages.success(request, 'User Register successfully!')
            return redirect("login")
        return render(request,'register.html',{'form':form})
    else:
        form=UserLoginForm(request.POST or None)
        context={"form":form}
        return render(request,'login.html',context)

def login_(request,*args,**kwargs):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        new_user=User.objects.get(email__iexact=form.cleaned_data.get('email'))
        login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
        # return redirect('index')
        if request.user.is_admin:
            return redirect('adminsdb')
        elif request.user.is_staff:
            return redirect('staffdb')
        elif request.user.is_medical:
            return redirect('medicaldb')
        elif request.user.is_lab:
            return redirect('labdb')
        elif request.user.is_doctor:
            id=request.user.id
            return redirect('doctordb')
        else:
            return redirect("login")

    return render(request,"login.html",{'form':form})

def logout_(request):
    logout(request)
    return redirect('login')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm( request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form,})
