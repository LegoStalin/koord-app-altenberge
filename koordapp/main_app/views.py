from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render

from django.shortcuts import redirect


class LoginInterfaceView(LoginView):
    template_name = 'user_verification/user_login.html'



class ResetPasswordMailView(View):
    template_name = 'user_verification/reset_pw_mail.html'
    def get(self, request):
        return render(request, self.template_name)
class SetNewPasswordView(View):
    template_name = 'user_verification/set_new_pw.html'
    def get(self, request):
        return render(request, self.template_name)
class ResetPasswordConfirmationView(View):
    template_name = 'user_verification/reset_pw_confirmation.html'
    def get(self, request):
        return render(request, self.template_name)

class HomeView(TemplateView):
    template_name = 'home/home.html'

class CreateActivityView(TemplateView):
    template_name = 'create_activity/create_activity.html'

