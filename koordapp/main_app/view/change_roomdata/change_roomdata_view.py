from django.shortcuts import redirect, render
from main_app.models import Raum, Raum_Belegung, Personal, AGKategorie
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

def change_roomdata_view(request):
    device_id = request.COOKIES.get('device_id')
    if(Raum_Belegung.objects.filter(tablet_id=device_id).exists()):
        raum_belegung = Raum_Belegung.objects.get(tablet_id=device_id)
        raum = raum_belegung.raum
        if not (raum_belegung.ag == None):
            ag = raum_belegung.ag
            personal = ag.leiter
            nutzer = personal.nutzer
            gruppenleiter_gruppe = Group.objects.get(name="Gruppenleitung")
            raumbetreuer_gruppe = Group.objects.get(name="Raumbetreuer")
            personallist = Personal.objects.filter(rechte_gruppe=gruppenleiter_gruppe) | Personal.objects.filter(rechte_gruppe=raumbetreuer_gruppe)

            if request.method == "POST":
                if 'change_button_user' in request.POST:
                    username = request.POST.get("user")
                    if(User.objects.filter(username=username).exists()):
                            user = User.objects.get(username=username)
                            personal = Personal.objects.get(user=user)
                            nutzer = personal.nutzer
                            ag.leiter = personal
                            ag.save()
                elif 'change_button_activity' in request.POST:
                    ag_name = request.POST.get("activity")
                    ag.name = ag_name
                    ag.save()
                elif 'change_button_category' in request.POST:
                    category_name = request.POST.get("category_name")
                    if AGKategorie.objects.filter(name=category_name).exists():
                        ag_kategorie = AGKategorie.objects.get(name=category_name)
                        ag.ag_kategorie = ag_kategorie
                        ag.save()
                elif 'change_button_capacity' in request.POST:
                    capacity = request.POST.get("capacity")
                    try:
                        capacity = int(capacity)
                        if(capacity<=raum.kapazitaet):
                            ag.max_anzahl = capacity
                            ag.save()
                    except:
                        pass    # Fehlermeldung ?
            return render(request, "change_roomdata/change_roomdata.html", {"room_name":raum.raum_nr, "nutzer":nutzer, "personallist":personallist, "ag":ag, "ag_kategorien":AGKategorie.objects.all()})
    
    return redirect("master_web")

    