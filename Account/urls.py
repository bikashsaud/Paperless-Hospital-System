from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, login_, logout_,change_password
# from django.contrib.auth import views as auth_views



urlpatterns = [
            url(r'^register/$',views.register,name='register'),
            url(r'^login_/$',views.login_,name='login'),
            url(r'^logout_/$',views.logout_,name='logout'),
            url(r'^password/$', views.change_password, name='change_password'),

            url(r'^oauth/', include('social_django.urls', namespace='social')),

            # url(r'^password_reset/$', views.password_reset, name='password_reset'),
            # url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
            # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.password_reset_confirm, name='password_reset_confirm'),
            # url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
            ]
