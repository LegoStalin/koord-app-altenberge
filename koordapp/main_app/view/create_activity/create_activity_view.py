from django.shortcuts import redirect, render
from main_app.models import Raum, Raum_Belegung, Personal, AGKategorie, AG
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib import messages

def create_activity_view(request, raum):
    if(Raum.objects.filter(raum_nr=raum).exists()):
        raum = Raum.objects.get(raum_nr=raum)
        if not(Raum_Belegung.objects.filter(raum=raum).exists()):
            if request.method == "POST":
                username_aufsichtsperson = request.POST["aufsichtsperson"]
                if(User.objects.filter(username=username_aufsichtsperson).exists()):
                    max_anzahl = request.POST["capacity"]
                    try:
                        max_anzahl = int(max_anzahl)
                        name_ag_kategorie = request.POST[""]
                        if AGKategorie.objects.filter(name=name_ag_kategorie).exists():
                            ag_kategorie = AGKategorie.objects.get(name=name_ag_kategorie)
                            name_activity = request.POST["activity"]
                            if AG.objects.filter(name=name_activity).exists():
                                ag = AG.objects.get(name=name_activity)
                                ag.ag_kategorie = ag_kategorie
                                ag.max_anzahl = max_anzahl
                                ag.save()
                            else:
                                
                                pass 
                        else:
<<<<<<< HEAD
                            # Error message wen kategorie nicht existiert
                            messages.error(request, 'AG Kategorie existiert nicht')
=======
                            # Error message wenn kategorie nicht existiert
>>>>>>> 37a3d68a1644b3480493a3b97125c4b50db1e5ed
                            pass
                    except ValueError:
                        #error message wenn capazitaet keine Zahl ist!
                        messages.error(request, 'Ungültige kapazitätsanzahl')
                        pass
            gruppenleiter_gruppe = Group.objects.get(name="Gruppenleitung")
            raumbetreuer_gruppe = Group.objects.get(name="Raumbetreuer")
            personallist = Personal.objects.filter(rechte_gruppe=gruppenleiter_gruppe) | Personal.objects.filter(rechte_gruppe=raumbetreuer_gruppe)
            return render(request, "create_activity/create_activity.html", {"room":raum, "personallist":personallist, "ag_kategorien":AGKategorie.objects.all()})

    return redirect("master_web")