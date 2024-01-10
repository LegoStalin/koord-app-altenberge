from django.urls import path
from django.views.generic import RedirectView
from . import views



urlpatterns = [
    path('master_web/', views.master_web, name='master_web'),
    path('master_tablet/', views.master_android, name='master_tablet'),
    path('remove_tablet/', views.remove_tablet, name='remove_tablet'),
    path('set_nfc_scan/', views.SetNfcScanAndroidView.as_view(), name='set_nfc_scan'),
    path('choose_room/', views.choose_room, name='choose_room'),
    path('create_activity/<str:raum>', views.create_activity, name='create_activity'),
    path('csv_import/', views.csv_import, name='csv_import'),
    path('change_roomdata/', views.change_roomdata, name='change_roomdata'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('superuser/', views.superuser, name='superuser'),
    path('set_new_pw/', views.set_new_pw, name='set_new_pw'),
    path('reset_pw_confirmation/', views.reset_pw_confirmation, name='reset_pw_confirmation'),
    path('pupil/<int:pupil>', views.pupil, name='pupil'),
    path('ogs_group/', views.ogs_group, name='ogs_group'),
    path('select_room/', views.select_room, name='select_room'),
    path('room_selection/<str:raum>', views.room_selection, name='room_selection'),
    path('room_information/<str:raum>', views.room_information, name='room_information'),
    path('preferences/', views.preferences, name='preferences'),
]


allowed_urls_android = [
    'master_tablet',
    'remove_tablet',
    'set_nfc_scan',
    'choose_room',
    'create_activity',
    'change_roomdata',
    'login',
    'logout',
    'set_new_pw',
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
    'login',
    'logout',
    'superuser',
    'set_new_pw',
    'reset_pw_confirmation',
    'pupil',
    'ogs_group',
    'select_room',
    'room_selection',
    'room_information',
    'preferences',
    ]
main_url_web = 'master_web'