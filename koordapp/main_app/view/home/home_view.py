from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from main_app.models import Raum_Belegung

def home_view(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request,"home/home.html")