from django.urls import path
from django.views.generic import RedirectView
from . import views



urlpatterns = [
    path('master_web/', views.MasterHomeView.as_view(), name='master_web'),
    path('choose_room/', views.choose_Room, name='choose_room'),
    path('choose_room/<int:raum_nr>', views.choose_RoomNr, name='choose_room_nr'),
]