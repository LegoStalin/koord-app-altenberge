from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect



class MasterHomeView(TemplateView):
    template_name = 'master_overview/master_web.html'

class ChooseRoomView(TemplateView):
    template_name = 'choose_room/choose_room.html'