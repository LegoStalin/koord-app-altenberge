from django.urls import path

from . import views
from .views import CreateActivityView
from .views import LoginInterfaceView


urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('create_activity/', views.CreateActivityView.as_view(), name='create_activity'),
    path('master_web/', views.MasterHomeView.as_view(), name='master_web')
]