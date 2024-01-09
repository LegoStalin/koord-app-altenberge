from django.urls import path
from django.views.generic import RedirectView
from . import views



urlpatterns = [
    path('master_web/', views.MasterHomeView.as_view(), name='master_web'),
    path('master_tablet/', views.MasterAndoridHomeView.as_view(), name='master_tablet'),
    path('remove_tablet/', views.RemoveTabletView.as_view(), name='remove_tablet'),
    path('set_nfc_scan/', views.SetNfcScanAndroidView.as_view(), name='set_nfc_scan'),
    path('choose_room/', views.ChooseRoomView.as_view(), name='choose_room'),
    path('create_activity/', views.CreateActivityView.as_view(), name='create_activity'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('checked_in/', views.CheckedInView.as_view(), name='checked_in'),
    path('checked_out/', views.CheckedOutView.as_view(), name='checked_out'),
    path('change_roomdata/', views.ChangeRoomDataView.as_view(), name='change_roomdata'),
    path('set_nfc_set/', views.SetNfcSetView.as_view(), name='set_nfc_set'),
    path('ogs_group/', views.OgsGroupView.as_view(), name='ogs_group'),
    path('search_pupil/', views.SearchPupilView.as_view(), name='search_pupil'),
    path('select_room/', views.SelectRoomView.as_view(), name='select_room'),
    path('room_selection/', views.RoomSelectionView.as_view(), name='room_selection'),
    path('room_information/', views.RoomInformationView.as_view(), name='room_information'),
    path('room_history/', views.RoomHistoryView.as_view(), name='room_history'),
    path('food_history/', views.FoodHistoryView.as_view(), name='food_history'),
    path('feedback_history/', views.FeedbackHistoryView.as_view(), name='feedback_history'),
    path('room_usage_history/', views.RoomUsageHistoryView.as_view(), name='room_usage_history'),
    path('pupil/', views.PupilView.as_view(), name='pupil'),
]