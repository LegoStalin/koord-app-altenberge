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
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Nutzer, Personal, Raum, Gruppe, AG, Schueler
from .view.csv_import.csv_import_view import csv_import_view
from .view.user_verification.login_view import login_view
from .view.user_verification.set_new_password_view import set_new_password_view
from .view.user_verification.su_pw_reset_view import su_pw_reset_view


class ResetPasswordMailView(View):
    template_name = 'user_verification/reset_pw_mail.html'
    def get(self, request):
        return render(request, self.template_name)
class ResetPasswordConfirmationView(View):
    template_name = 'user_verification/reset_pw_confirmation.html'
    def get(self, request):
        return render(request, self.template_name)

class HomeView(TemplateView):
    template_name = 'home/home.html'

class CreateActivityView(TemplateView):
    template_name = 'create_activity/create_activity.html'

class MasterHomeView(TemplateView):
    template_name = 'master_overview/master_web.html'

def su_pw_reset(request):
    return su_pw_reset_view(request)

def set_new_password(request):
    return set_new_password_view(request)

def csv_import(request):
    return csv_import_view(request)

def roomplan(request):
    return render(request, 'room_plan/room_overview.html', {'rooms':Raum.objects.all()})

def login(request):
    return login_view(request)

