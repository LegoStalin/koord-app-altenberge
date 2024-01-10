from django.shortcuts import redirect, render
from main_app.models import Raum_Belegung, Aufenthalt, Raum_Historie
from datetime import datetime

def remove_tablet_view(request):
    if request.method == 'POST':
        if 'submit_rr' in request.POST:
            device_id = request.COOKIES.get('device_id')
            if(Raum_Belegung.objects.filter(tablet_id=device_id).exists()):
                raum_belegung = Raum_Belegung.objects.get(tablet_id=device_id)
                raum = raum_belegung.raum
                if(Aufenthalt.objects.filter(raum_nr=raum, zeitraum__endzeit=None).exists):
                    aufenthalte = Aufenthalt.objects.filter(raum_nr=raum, zeitraum__endzeit=None)
                    for aufenthalt in aufenthalte:
                        aufenthalt.zeitraum.endzeit = datetime.now().time()
                        aufenthalt.save()
                zeitraum = raum_belegung.ag.zeitraum
                zeitraum.endzeit = datetime.now().time()
                zeitraum.save()
                raum_historie = Raum_Historie.objects.create(zeitraum=zeitraum,raum=raum,tag=datetime.now().date(),ag_name=raum_belegung.ag.name,ag_kategorie=raum_belegung.ag.ag_kategorie.name,leiter=raum_belegung.ag.leiter)
                raum_belegung.delete()
                return redirect('choose_room')
        elif 'abort_rr' in request.POST:
            return redirect('master_tablet')
    return render(request, "master_android/remove_tablet.html")