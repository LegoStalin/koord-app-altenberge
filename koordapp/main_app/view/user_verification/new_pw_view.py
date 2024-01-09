from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import logout

def new_pw_view(request):
    return render(request, "user_verification/new_pw.html")