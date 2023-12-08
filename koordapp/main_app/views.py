import string, random
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
=======
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render
>>>>>>> main

from django.shortcuts import redirect
from django.shortcuts import render

from .models import Nutzer, Personal, Raum, Gruppe, AG, Schueler
from .view.csv_import.csv_import_view import csv_import_view



<<<<<<< HEAD
=======
class LoginInterfaceView(LoginView):
    template_name = 'user_verification/user_login.html'



class ResetPasswordMailView(View):
    template_name = 'user_verification/reset_pw_mail.html'
    def get(self, request):
        return render(request, self.template_name)
class SetNewPasswordView(View):
    template_name = 'user_verification/set_new_pw.html'
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
>>>>>>> main

<<<<<<< HEAD
class MasterHomeView(TemplateView):
    template_name = 'master_overview/master_web.html'
=======
<<<<<<< HEAD
def csv_import(request):
    return csv_import_view(request)

def roomplan(request):
    return render(request, 'room_plan/room_overview.html', {'rooms':Raum.objects.all()})
=======
>>>>>>> main
>>>>>>> main
