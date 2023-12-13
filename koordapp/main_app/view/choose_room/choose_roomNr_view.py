from django.shortcuts import redirect, render
from main_app.models import Raum, Raum_Belegung

def choose_roomNr_view(request, raum_nr):

    return render(request, "choose_room/create_activity.html")