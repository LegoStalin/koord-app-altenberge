from django.shortcuts import redirect, render
from main_app.models import Raum, Raum_Belegung, Personal, AGKategorie, AG
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib import messages

# @login_required(login_url="/login")
def create_activity_view(request, raum):
    if(Raum.objects.filter(raum_nr=raum).exists()):
        raum = Raum.objects.get(raum_nr=raum)
        device_id = request.COOKIES.get('device_id')
        if not(Raum_Belegung.objects.filter(tablet_id=device_id).exists()):
            if not(Raum_Belegung.objects.filter(raum=raum).exists()):
                if request.method == "POST":
                    username_aufsichtsperson = request.POST["aufsichtsperson"]
                    if(User.objects.filter(username=username_aufsichtsperson).exists()):
                        user = User.objects.get(username=username_aufsichtsperson)
                        aufsichtsperson = Personal.objects.get(user=user)
                        max_anzahl = request.POST["capacity"]
                        try:
                            max_anzahl = int(max_anzahl)
                            name_ag_kategorie = request.POST["ag_kategorie"]
                            if AGKategorie.objects.filter(name=name_ag_kategorie).exists():
                                ag_kategorie = AGKategorie.objects.get(name=name_ag_kategorie)
                                name_activity = request.POST["activity"]
                                
                                ag = AG.objects.create(name=name_activity, max_anzahl=max_anzahl,offene_AG=True,leiter=aufsichtsperson,ag_kategorie=ag_kategorie)
                                raum_belegung = Raum_Belegung.objects.create(raum=raum, ag=ag, tablet_id=device_id)
                                return redirect("choose_room")  # Weiterleitung bei erfolgreichen erstellen des raumes
                            else:
                                # Error message wen kategorie nicht existiert
                                messages.error(request, 'AG Kategorie existiert nicht')
                        except ValueError:
                            #error message wenn capazitaet keine Zahl ist!
                            messages.error(request, 'Ungültige kapazitätsanzahl')
                    else:
                        messages.error(request, 'Ungültige Personaleingabe')
                gruppenleiter_gruppe = Group.objects.get(name="Gruppenleitung")
                raumbetreuer_gruppe = Group.objects.get(name="Raumbetreuer")
                personallist = Personal.objects.filter(rechte_gruppe=gruppenleiter_gruppe) | Personal.objects.filter(rechte_gruppe=raumbetreuer_gruppe)
                return render(request, "create_activity/create_activity.html", {"room":raum, "personallist":personallist, "ag_kategorien":AGKategorie.objects.all()})
        
            else:
                pass

    return redirect("master_web")