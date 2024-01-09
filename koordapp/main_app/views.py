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

class MasterHomeView(TemplateView):
    template_name = 'master_overview/master_web.html'

class MasterAndoridHomeView(TemplateView):
    template_name = 'master_android/master_tablet.html'

class RemoveTabletView(TemplateView):
    template_name = 'master_android/remove_tablet.html'

class SetNfcScanAndroidView(TemplateView):
    template_name = 'master_android/set_nfc_scan.html'

class ChooseRoomView(TemplateView):
    template_name = 'choose_room/choose_room.html'

class CreateActivityView(TemplateView):
    template_name = 'create_activity/create_activity.html'

def choose_room(request):
    return choose_room_view(request)

def create_activity(request, raum):
    return create_activity_view(request, raum)

def csv_import(request):
    return csv_import_view(request)

def change_roomdata(request):
    return change_roomdata_view(request)