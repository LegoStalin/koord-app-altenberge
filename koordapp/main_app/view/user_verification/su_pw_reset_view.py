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
def su_pw_reset_view(request):
    user = request.user
    # user = User.objects.get(user = user)
    if(user.is_superuser):
        if request.method == "POST":
            nutzername = request.POST["reset_button"]
            randompw = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(6))
            nutzer = User.objects.get(username=nutzername)
            nutzer.set_password(randompw)
            nutzer.save()
            personal = Personal.objects.get(user=nutzer)
            personal.is_password_otp = True
            personal.save()
            messages.success(request, "Das neue OTP für den Nutzer " + nutzername +  " ist " + randompw)
        return render(request, "user_verification/su_pw_reset.html", {"allPersonal":Personal.objects.all()})
    return redirect("master_web")