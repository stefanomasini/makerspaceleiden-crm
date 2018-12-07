from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from members.models import Member
from acl.models import Machine,Instruction
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record_instructions/', views.recordinstructions, name='add_instruction'),
    path('userdetails/', views.userdetails, name='userdetails'),
    # for the password reset by email.
    re_path('^registration/', include('django.contrib.auth.urls')),
]

