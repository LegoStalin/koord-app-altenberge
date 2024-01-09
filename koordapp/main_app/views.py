from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from main_app.view.csv_import.csv_import_view import csv_import_view

from django.shortcuts import redirect



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

class HomeView(TemplateView):
    template_name = 'home/home.html'

class CheckedInView(TemplateView):
    template_name = 'checked_in/checked_in.html'

class CheckedOutView(TemplateView):
    template_name = 'checked_out/checked_out.html'

def csv_import(request):
    return csv_import_view(request)