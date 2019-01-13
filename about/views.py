from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .import views
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import StaffForm,MedicalForm,LabForm,DoctorForm,AdminForm,DoctorUpdateForm,EditProfileForm,EditAProfileForm,PatientForm,D_MedicalForm,D_LabForm,MedicineForm,Test_resultForm
from doctor.models import doctor as mydoctor
from lab.models import lab
from Patient_Profile.models import Patient,D_Medical
from medical.models import medical as mymedical
from staff.models import Staff
from superadmin.models import superadmin as mysuperadmin
from Account.models import UserProfile

from django.db.models import Q
# from example.config import pagination
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf


# Create your views here.

def staffdb(request):
    if request.user.is_staff:
        form=Patient.objects.all()
        con={"form":form,}
        return render(request,"staffdb.html",con)
    # return render(request,"staffdb.html")
def medical(request):
    return render(request,'medicaldb.html')
def lab(request):
    return render(request,"labdb.html")

def doctordb(request):
    if request.user.is_authenticated():
        query=Patient.objects.all()[:3]
        # ins=mydoctor.objects.get(user_id=request.user.id)
        question=request.GET.get("q")
        if question:
            query=Patient.objects.all()
            query=query.filter(
            Q(name__icontains=question)
            ).distinct() #use name__iexact when exact value is required
        context={"query":query,}
        if request.user.is_doctor:
            return render(request,'doctordb.html',context)
        elif request.user.is_medical:
            return render(request,'medicaldb.html',context)
        elif request.user.is_lab:
            return render(request,'labdb.html',context)
    else:
        return render(request,'login')
#
# @login_required
def adminsdb(request):
    if request.user.is_admin:
        quer=Patient.objects.all()[:5]

        # qu=UserProfile.objects.filter(is_doctor=True)
        query_set=mydoctor.objects.all()[:5]

        query_set1=Staff.objects.all()[:6]
        # qu1=UserProfile.objects.filter(is_staff=True)

        ins=mysuperadmin.objects.get(user=request.user.id)

        question=request.GET.get("q")
        if question:
            query=UserProfile.objects.all()
            print(query)
            q1=query.filter(
            Q(name__icontains=question)
            ).distinct()

        context={'u':query_set,"query":quer,"v":query_set1,"ins":ins,}
        return render(request,'admindb.html',context)

@login_required()
def editadminprofile(request):
    # if request.user.is_admin:
    users=UserProfile.objects.get(id=request.user.id)
    doct=mysuperadmin.objects.get(user=users.id)
    form=AdminForm(request.POST or None, instance=doct)
    forms=DoctorUpdateForm(request.POST or None, instance=users)
    if form.is_valid() and forms.is_valid():
        form.save()
        forms.save()
        return redirect('adminsdb')

    context= {'form':form,
            'forms':forms,
            }
    return render(request,'editadmin.html',context)

@login_required()
def editdoctorprofile(request):

# if request.user.is_doctor:
    users=UserProfile.objects.get(id=request.user.id)
    doct=mydoctor.objects.get(user=users.id)
    form=DoctorForm(request.POST or None ,instance=doct)
    forms=DoctorUpdateForm(request.POST or None,instance=users)
    if form.is_valid() and forms.is_valid():
        form.save()
        forms.save()
        return redirect('doctordb')

    context = {'form':form,
            'forms':forms,
            'doct':doct, #to show image in profile
         }
    return render(request,'editdoctor.html',context)

def editlab(request):
    pass
    # if request.user.is_lab:
    #     form=LabForm(request.POST or None,)


def profilepicture(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('doctordb')
    else:
        form = UploadFileForm()
    return render(request, 'doctordb.html', {'form': form})

@login_required()
def show_profile(request):
    if request.user.is_doctor:
        return render(request,'show_doctorprofile.html')
    else:
        return HttpResponse('<h1>NOT FOUND PAGE</h1>')

@login_required()
def show_adminprofile(request):
    if request.user.is_admin:
        ins=mysuperadmin.objects.get(user=request.user.id)
        con={'con':ins,}
        return render(request,'show_adminprofile.html',con)
    else:
        return HttpResponse('<h1>NOT FOUND PAGE</h1>')


def all_doctors(request):
    if request.user.is_authenticated():
        doct=mydoctor.objects.all()
        query=UserProfile.objects.filter(is_doctor=True)
        args={'doctor':zip(doct,query),}
        return render(request,'all_doctor.html',args)

def patient_list(request):
    if request.user.is_authenticated():
        d=Patient.objects.all()
        return render(request,'all_patient.html',{"d":d,})


def staff_list(request):
    if request.user.is_authenticated():
        doct=Staff.objects.all()
        args={'doctor':doct,}
        return render(request,'all_staff.html',args)


def delete_doctor(request,id):
	if request.user.is_authenticated():
		try:
			doct=UserProfile.objects.get(id=id)
			doct.delete()
			return redirect('all_doctors')
		except:
			return redirect('all_doctors')
	else:
		return redirect('login')


def delete_staff(request,id):
	if request.user.is_authenticated():
		try:
			doct=UserProfile.objects.get(id=id)
			doct.delete()
			return redirect('staff_list')
		except:
			return redirect('staff_list')
	else:
		return redirect('login')

def view_doctor(request,id):
    if request.user.is_authenticated():
        doct = mydoctor.objects.get(id=id)
        # staff=staff.objects.get(id=id)
        con={'doct':doct,}
        return render(request,'show_doctor.html',con)

# =========================================
#                   ADD NEW Patient
# =========================================
def patient_register(request):
    if request.user.is_staff:
        form=PatientForm(request.POST or None)
        args={"form":form,}
        if form.is_valid():
            form.save()
            return redirect('staffdb')
        return render(request,'register_patient.html',args)



def treatment(request,id):
    if request.user.is_authenticated():
        form=Patient.objects.get(id=id)
        form1=D_Medical.objects.filter(patient_id=id).order_by('-date')
        form2=D_MedicalForm(request.POST or None)
        profile=mydoctor.objects.get(user=request.user.id)
        if form2.is_valid():
            abc=form2.save(commit=False)
            abc.doctor_id=profile.id
            abc.patient_id=id
            form2.save()
            return redirect("doctordb")
        context={"form":form,'form1':form1,"form2":form2,}
        return render(request,'treatment.html',context)
    else:
        return redirect("login")

def medicine(request,id):
    if request.user.is_authenticated():
        mform=D_MedicalForm(request.POST or None)
        # patient=Patient.objects.get(id=id)
        # user=UserProfile.objects.get(id=request.user.id)
        profile=mydoctor.objects.get(user=request.user.id)
        if mform.is_valid():
            abc=mform.save(commit=False)
            abc.doctor_id=profile.id
            abc.patient_id=id
            mform.save()
            return redirect("doctordb")
        context={"mform":mform,'id':id,}
        return render(request,'medicines.html',context)

def tests(request):
    if request.user.is_authenticated():
        mform=D_LabForm(request.POST or None)
        profile=mydoctor.objects.get(user=request.user.id)
        if mform.is_valid():
            abc=mform.save(commit=False)
            abc.doctor_id=profile.id
            abc.patient_id=id
            abc.save()
            return redirect("doctordb")
        context={"mform":mform,}
        return render(request,'tests.html',context)

def give_medicines(request,id):
    if request.user.is_authenticated():
        form=Patient.objects.get(id=id)
        lform=D_Medical.objects.filter(patient=id).last()
        # user=UserProfile.objects.get(id=request.user.id)
        profile=mymedical.objects.get(user=request.user.id)
        print(profile)
        mform=MedicineForm(request.POST or None)
        if mform.is_valid():
            abc=mform.save(commit=False)
            abc.patient_id=id
            abc.medical_id=profile.id
            abc.save()
            return redirect("doctordb")
        context={"form":form,
                    "lform":lform,
                    "mform":mform,
                    }
        return render(request,'give_medicines.html',context)
    else:
        return redirect("login")


def Test_result(request,id):
    if request.user.is_authenticated():
        form=Patient.objects.get(id=id)
        lform=D_Lab.objects.latest("id")
        mform=Test_resultForm(request.POST or None)
        if mform.is_valid():
            mform.save()
            return redirect('labdb')
        context={"form":form,
                    "lform":lform,
                    "mform":mform,
                    }
        return render(request,'Test_result.html',context)
    else:
        return redirect("login")


def Test_result(request):
    if request.user.is_authenticated():
        form=Test_resultForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("medicaldb")
        con={"form":form,}
        return render(request,'Test_result.html',con)


def patientview_profile(request,id):
    if request.user.is_authenticated():
        form=Patient.objects.get(id=id)
        con={"form":form,}
        return render(request,'patient_profile.html',con)
    else:
        return redirect('login')


def sview_profile(request,id):
    if request.user.is_authenticated():
        form=Staff.objects.get(id=id)
        con={"form":form,}
        return render(request,'staff_profile.html',con)
    else:
        return redirect('login')
# =================================
# pdf downloadable FILES
# =================================


def pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    return FileResponse(buffer)
 #created in step 4

def gpdf(request, *args, **kwargs):
    data = {
         'today': "datetime.date.today()",
         'amount': 3900,
        'medical_name': 'Milan Saud',
        'order_id': 1233434,
    }
    pdf = render_to_pdf('pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
