from django.forms import ModelForm
from django import forms
from staff.models import Staff
from medical.models import medical
from lab.models import lab
from doctor.models import doctor
from superadmin.models import superadmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from Account.models import UserProfile
from django.contrib.auth import authenticate, get_user_model
from Patient_Profile.models import Patient,D_Medical,D_Lab,Test_result,Medicine

User=get_user_model()
# from .models import User


class StaffForm(forms.ModelForm):
	class Meta:
		model=Staff
		fields=['phoneno','address','sex','age','post','image','cv','Portfolio','degree','join_date']

		labels={
		"phoneno":"Phone No.","address":"Address",
		"sex":"Sex","age":"Age","post":"Post","image":"Image",
		"cv":"CV","Portfolio":"Portfolio","degree":"Degree","join_date":"Join Date",
		}
		help_text={
		"phoneno":"enter phone no",
		"address":"Enter your address","age":"Enter age","post":"Job detail",
		"image":"select image","Portfolio":"enter your Portfolio Link Here","join_date":"Date",
		}
class MedicalForm(forms.ModelForm):
	"""docstring for medicalform."""
	class Meta:
		model=medical
		fields="__all__"

	# def __init__(self, arg):
	# 	super(medicalform, self).__init__()
	# 	self.arg = arg
class LabForm(forms.ModelForm):
	class Meta:
		model=lab
		fields="__all__"
class DoctorForm(forms.ModelForm):
	# phoneno=forms.CharField(label='Phone no.',widget=forms.IntegerInput(attrs={"class":'form-control'}))


	class Meta:
		model=doctor
		exclude=["user","t_address","join_date",'experience',"cv","university","degree"]
		# fields="__all__"

class PatientForm(forms.ModelForm):
	class Meta:
		model=Patient
		# fields='__all__'
		fields=["name","phoneno","address","sex","age","date","about","user"]

# class PatientCreationForm(forms.ModelForm):
#
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email', 'name',)
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Enter Correct Password")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

class DoctorUpdateForm(forms.ModelForm):
	email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={"class":'form-control'}))
	name=forms.CharField(label='Name',widget=forms.TextInput(attrs={"class":'form-control'}))
	# password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":'form-control'}))
	# password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={"class":'form-control'}))

	class Meta:
		"""docstring for meta."""
		model=UserProfile
		fields=['email','name',]


class AdminForm(forms.ModelForm):
	class Meta:
		model=superadmin
		exclude=["user","t_address","join_date",'experience',"cv","university","degree"]

class EditProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=['email','name']
class EditAProfileForm(forms.ModelForm):
	class Meta:
		model=superadmin
		fields=('phoneno',
		'p_address',
		't_address',
		'join_date',
		'post',
		'age'
		)
	def save(self,commit=True):
		 user = super(EditAProfileForm, self).save(commit=False)
		 user.phoneno = self.cleaned_data['phoneno']
		 user.p_address = self.cleaned_data['p_address']
		 user.t_address = self.cleaned_data['t_address']
		 user.join_date = self.cleaned_data['join_date']
		 user.post = self.cleaned_data['post']
		 user.age = self.cleaned_data['age']
		 if commit:
			 user.save()
			 return user


class D_MedicalForm(forms.ModelForm):
	class Meta:
		model=D_Medical
		exclude=['doctor','patient']
		# fields='__all__'

class D_LabForm(forms.ModelForm):
	class Meta:
		model=D_Lab
		exclude=['doctor','patient',]
		# fields='__all__'

class MedicineForm(forms.ModelForm):
	class Meta:
		model=Medicine
		exclude=['patient','medical']

class Test_resultForm(forms.ModelForm):
	class Meta:
		model=Test_result
		fields='__all__'
