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
from django import forms

from main_app.models import Nutzer, Personal, Raum, Gruppe, AG, Schueler

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            cleandata=form.cleaned_data
            #authenticate checks if credentials exists in db
            user=authenticate(username=cleandata['username'],
                            password=cleandata['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect("home")
            else:
                return redirect("login")
        else:
            print('')
    form=AuthenticationForm()
    return render(request, "user_verification/user_login.html", {'form':form})