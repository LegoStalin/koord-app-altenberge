from django.urls import path
from .views import CreateActivityView
from . import views


urlpatterns = [ 
    path('master_web/', views.MasterHomeView.as_view(), name='master_web'),
    path('master_tablet/', views.MasterAndoridHomeView.as_view(), name='master_tablet'),
    path('remove_tablet/', views.remove_tablet, name='remove_tablet'),
    path('set_nfc_scan/', views.SetNfcScanAndroidView.as_view(), name='set_nfc_scan'),
    path('choose_room/', views.choose_room, name='choose_room'),
    path('create_activity/<str:raum>', views.create_activity, name='create_activity'),
    path('csv_import/', views.csv_import, name='csv_import'),
    path('change_roomdata/', views.change_roomdata, name='change_roomdata'),
]


allowed_urls_android = [
    'master_tablet',
    'remove_tablet',
    'set_nfc_scan',
    'choose_room',
    'create_activity',
    'change_roomdata',
    ]
main_url_android = 'master_tablet'

allowed_urls_android_no_room = [
    'choose_room',
    'create_activity',
    ]
main_url_android_no_room = 'choose_room'

allowed_urls_web = [
    'master_web',
    'csv_import',
    ]
main_url_web = 'master_web'