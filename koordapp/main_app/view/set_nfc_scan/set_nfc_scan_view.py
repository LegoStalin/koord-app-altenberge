from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name="login")
def set_nfc_scan_view(request):
    return render("master_android/set_nfc_scan")