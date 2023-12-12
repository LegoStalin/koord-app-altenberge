from django.urls import path
from django.views.generic import RedirectView
from . import views



urlpatterns = [
    path('master_web/', views.MasterHomeView.as_view(), name='master_web'),
    path('master_tablet/', views.MasterAndoridHomeView.as_view(), name='master_tablet'),
    path('remove_tablet/', views.RemoveTabletView.as_view(), name='remove_tablet'),
    path('set_nfc_scan/', views.SetNfcScanAndroidView.as_view(), name='set_nfc_scan'),
    path('choose_room/', views.ChooseRoomView.as_view(), name='choose_room'),
    path('create_activity/', views.CreateActivityView.as_view(), name='create_activity')

]