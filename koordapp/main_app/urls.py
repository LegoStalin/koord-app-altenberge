from django.urls import path

from . import views
from .views import CreateActivityView
from .views import LoginInterfaceView


urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('create_activity/', CreateActivityView.as_view(), name='create_activity'),
    path('reset_password_mail/', views.ResetPasswordMailView.as_view(), name='reset_password_mail'),
    path('reset_password_confirmation/', views.ResetPasswordConfirmationView.as_view(), name='reset_password_confirmation'),
    path('set_new_password/', views.SetNewPasswordView.as_view(), name='set_new_password'),
]