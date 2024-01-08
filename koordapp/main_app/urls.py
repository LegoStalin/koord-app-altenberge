from django.urls import path
from .views import CreateActivityView
from . import views


urlpatterns = [ 
    path('master_web/', views.MasterHomeView.as_view(), name='master_web'),
    path('master_tablet/', views.MasterAndoridHomeView.as_view(), name='master_tablet'),
    path('remove_tablet/', views.RemoveTabletView.as_view(), name='remove_tablet'),
    path('set_nfc_scan/', views.SetNfcScanAndroidView.as_view(), name='set_nfc_scan'),
    path('choose_room/', views.choose_room, name='choose_room'),
    path('create_activity/<str:raum>', views.create_activity, name='create_activity'),
    path('csv_import/', views.csv_import, name='csv_import'),
]