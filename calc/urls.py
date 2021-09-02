from django.urls import path
from . import views

urlpatterns = [
    path('',views.projectclinic,name='projectclinic'),
    path('projectclinic',views.projectclinic,name='projectclinic'),
    path('login', views.login , name='login'),
    path('register',views.register , name='register'),
    path('pd',views.pd , name='pd'),
    path('patientinfo',views.patientinfo,name='patientinfo'),
]