from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from about.forms import DoctorForm
from HealthProblem.forms import CommentForm
from doctor.models import doctor
from Account.models import UserProfile
from UserComment.models import Comment


def index( request):
    if request.user.is_authenticated():
        com=Comment.objects.all()
        return render(request,'index.html',{"com":com, })

    else:
        form=CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')

        con={"form":form,}
    return render(request,'index.html',con)

def contact(request):
    return render(request,'contact.html')
