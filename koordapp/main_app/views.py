from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

from main_app.view.choose_room.choose_room_view import choose_room_view
from main_app.view.create_activity.create_activity_view import create_activity_view
from main_app.view.csv_import.csv_import_view import csv_import_view
from main_app.view.change_roomdata.change_roomdata_view import change_roomdata_view
from main_app.view.remove_tablet.remove_tablet_view import remove_tablet_view
from main_app.view.user_verification.login_view import login_view
from main_app.view.user_verification.logout_view import logout_view
from main_app.view.user_verification.su_pw_reset_view import su_pw_reset_view
from main_app.view.user_verification.set_new_password_view import set_new_password_view
from main_app.view.user_verification.reset_pw_confirmation_view import reset_pw_confirmation_view

class MasterHomeView(TemplateView):
    template_name = 'master_overview/master_web.html'

class MasterAndoridHomeView(TemplateView):
    template_name = 'master_android/master_tablet.html'

def remove_tablet(request):
    return remove_tablet_view(request)

class SetNfcScanAndroidView(TemplateView):
    template_name = 'master_android/set_nfc_scan.html'

def choose_room(request):
    return choose_room_view(request)

def create_activity(request, raum):
    return create_activity_view(request, raum)

def csv_import(request):
    return csv_import_view(request)

def change_roomdata(request):
    return change_roomdata_view(request)

def login(request):
    return login_view(request)

def logout(request):
    return logout_view(request)

def superuser(request):
    return su_pw_reset_view(request)

def set_new_pw(request):
    return set_new_password_view(request)

def reset_pw_confirmation(request):
    return reset_pw_confirmation_view(request)