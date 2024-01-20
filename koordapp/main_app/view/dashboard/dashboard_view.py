from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name="login")
def dashboard_view(request):
    return render("dashboard/dashboard.html")