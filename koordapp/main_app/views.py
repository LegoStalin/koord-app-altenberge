from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.shortcuts import redirect


class LoginInterfaceView(LoginView):
    template_name = 'login/login.html'

class HomeView(TemplateView):
    template_name = 'home/home.html'

class CreateActivityView(TemplateView):
    template_name = 'create_activity/create_activity.html'

def csv_import(request):
    return render(request, 'csv_import/csv_import.html')