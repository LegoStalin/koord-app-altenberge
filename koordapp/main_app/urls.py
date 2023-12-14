from django.urls import path
from django.views.generic import RedirectView
from . import views



urlpatterns = [
    path('master_web/', views.MasterHomeView.as_view(), name='master_web'),
    path('choose_room/', views.choose_Room, name='choose_room'),
    path('create_activity/<int:raum_nr>', views.choose_Room, name='create_activity'),  # TODO Methode anpassen!!
]