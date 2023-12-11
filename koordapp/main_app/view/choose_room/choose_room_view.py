from django.shortcuts import redirect, render
from main_app.models import Raum, Raum_Belegung

def choose_room_view(request):
    return render(request, "choose_room/choose_room.html", {"rooms":Raum.objects.all(), "room_occupancy":Raum_Belegung})