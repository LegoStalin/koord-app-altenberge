from django.urls import path
from .views import CreateActivityView
from . import views


urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),


    path('login/', views.login, name='login'),


    path('create_activity/', views.CreateActivityView.as_view(), name='create_activity'),


    path('master_web/', views.MasterHomeView.as_view(), name='master_web'),


    # path('csv_import/', views.csv_import, name='csv_import'),
    # path('roomplan/', views.roomplan, name='roomplan'),
    path('reset_password_mail/', views.ResetPasswordMailView.as_view(), name='reset_password_mail'),
    path('reset_password_confirmation/', views.ResetPasswordConfirmationView.as_view(), name='reset_password_confirmation'),
    path('set_new_password/', views.set_new_password, name='set_new_password')
]