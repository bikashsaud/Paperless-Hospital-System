from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login,logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete


urlpatterns=[
url(r'^staffdb/',views.staffdb,name='staffdb'),
url(r'^medical/',views.medicaldb,name='medicaldb'),
url(r'^lab/',views.labdb,name='labdb'),
url(r'^doctor/',views.doctordb,name='doctordb'),
url(r'^adminsdb/',views.adminsdb,name='adminsdb'),
url(r'^editadminprofile/',views.editadminprofile,name='editadminprofile'),
url(r'^editlab/',views.editlab,name='editlab'),


url(r'^profilepicture/',views.profilepicture,name='profilepicture'),
url(r'^showdoctorprofile/',views.show_profile,name='show_profile'),
# url(r'^edit_profile/$',views.edit_profile,name="edit_profile"),
url(r'^showadminprofile/',views.show_adminprofile,name='show_adminprofile'),

url(r'^doctoredit/(?P<id>[0-9]+)/$',views.editdoctorprofile,name='editdoctorprofile'),
url(r'^medicaledit/',views.editmedicalprofile,name='editmedicalprofile'),


url(r'^staff_list/(?P<id>[0-9]+)/$',views.delete_staff,name="delete_staff"),
url(r'^all_doctors/(?P<id>[0-9]+)/$',views.delete_doctor,name="delete_doctor"),

# url(r'^view_doc/(?P<id>[0-9]+)/$',views.view_doc,name="view_doc"),

url(r'^patient_register/', views.patient_register, name='patient_register'),
# url(r'^patient_list/', views.patient_list, name='patient_list'),
url(r'^treatment/(?P<id>[0-9]+)/$',views.treatment,name="treatment"),
# url(r'^medicine/(?P<id>[0-9]+)/',views.medicine,name="medicine"),
url(r'^give_medicines/(?P<id>[0-9]+)/$',views.give_medicines,name="give_medicines"),#to give medicine by medical to patient

url(r'^tests/(?P<id>[0-9]+)/$',views.tests,name="tests"), #to set lab test by doctors
url(r'^Test_result/(?P<id>[0-9]+)/$',views.Test_result,name="Test_result"),# to do testes of patients by LAB

url(r'^view_doctor/(?P<id>[0-9]+)/$',views.view_doctor,name="view_doctor"),
url(r'^patientview_profile/(?P<id>[0-9]+)/$',views.patientview_profile,name="patientview_profile"),
url(r'^sview_profile/(?P<id>[0-9]+)/$',views.sview_profile,name="sview_profile"),

url(r'^all_doctors/$', views.all_doctors, name='all_doctors'),
url(r'^staff_list/$', views.staff_list, name='staff_list'),
url(r'^patient_list/$', views.patient_list, name='patient_list'),

#to download in the pdf format
# url(r'^pdfview/$', views.pdf, name='pdf'),
url(r'^pdfgenerate/$', views.gpdf, name='gpdf'),
url(r'^DownloadBill/(?P<id>[0-9]+)/', views.DownloadBill, name='DownloadBill'),
url(r'^bill/(?P<id>[0-9]+)/', views.bill, name='bill'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
