from django.urls import path

from . import views



urlpatterns = [
    path('master_web/', views.MasterHomeView.as_view(), name='master_web')
]

urlpatterns = [
    path('choose_room/', views.ChooseRoomView.as_view(), name='choose_room')
]