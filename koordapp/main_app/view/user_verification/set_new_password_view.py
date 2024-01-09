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

@login_required(redirect_field_name='login')
def set_new_password_view(request):
    user = request.user
    if request.method == "POST":
        if(Personal.objects.filter(user=user).exists()):
            personal = Personal.objects.get(user=user)
            if(personal.is_password_otp):
                passwort1 = request.POST["new_password"]
                passwort2 = request.POST["repeat_new_password"]
                if(passwort1 == passwort2):
                    if(len(str(passwort1))>=5):       # TODO: Passwort requirements                       
                        user.set_password(passwort1)
                        user.save()
                        personal.is_password_otp = False
                        personal.save()
                        return redirect("master_web")
                    else:
                        messages.error(request,"Passwörter erfüllen nicht die bedingungen") 
                else:
                    messages.error(request,"Passwoörter stimmen nicht überein")
        else:
            pass    #Wenn kein OTP

    return render(request, "user_verification/set_new_pw.html")