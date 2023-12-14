from django.shortcuts import redirect, render
from main_app.models import Raum, Raum_Belegung, Personal, AGKategorie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

def create_activity_view(request, raum):
    if request.method == "POST":
        pass
    if(Raum.objects.filter(raum_nr=raum).exists()):
        raum = Raum.objects.get(raum_nr=raum)
        if not(Raum_Belegung.objects.filter(raum=raum).exists()):
            gruppenleiter_gruppe = Group.objects.get(name="Gruppenleitung")
            raumbetreuer_gruppe = Group.objects.get(name="Raumbetreuer")
            personallist = Personal.objects.filter(rechte_gruppe=gruppenleiter_gruppe) | Personal.objects.filter(rechte_gruppe=raumbetreuer_gruppe)
            return render(request, "create_activity/create_activity.html", {"room":raum, "personallist":personallist, "ag_kategorien":AGKategorie.objects.all()})

    return redirect("master_web")