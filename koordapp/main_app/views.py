import string, random
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import redirect
from django.shortcuts import render

from .models import Nutzer, Personal, Raum, Gruppe, AG, Schueler
from .view.csv_import.csv_import_view import csv_import_view



class LoginInterfaceView(LoginView):
    template_name = 'login/login.html'

class HomeView(TemplateView):
    template_name = 'home/home.html'

class CreateActivityView(TemplateView):
    template_name = 'create_activity/create_activity.html'

def csv_import(request):
    return csv_import_view(request)

def roomplan(request):
    return render(request, 'room_plan/room_overview.html', {'rooms':Raum.objects.all()})