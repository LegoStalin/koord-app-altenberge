from django.shortcuts import redirect, render
from main_app.models import Schueler, Nutzer, Aufenthalt, Raum_Belegung, Gruppe

# ! Berechtigungsmanagment fehlt!
def pupil_view(request, pupil):

    if Nutzer.objects.filter(id=pupil).exists():
        nutzer = Nutzer.objects.get(id=pupil)
        if Schueler.objects.filter(user_id=nutzer).exists():
            schueler = Schueler.objects.get(user_id=nutzer)

            if schueler.bus_kind == True:
                bus_kind = 'Ja'
            else:
                bus_kind = 'Nein'

            aufenthalt = "Abgemeldet"
            aktuelle_ag = "Keine"
            if schueler.angemeldet == True:
                if(Aufenthalt.objects.filter(schueler_id=schueler).exists()):
                    aufenthalte = Aufenthalt.objects.get(schueler_id=schueler)
                    if(aufenthalte.zeitraum.filter(endzeit=None).exists()):
                        aufenthalt = aufenthalte.zeitraum.get(endzeit=None)
                        raum = aufenthalt.raum_id
                        aufenthalt = "Raum " + raum.raum_nr
                        if(Raum_Belegung.objects.filter(raum=raum).exists):
                            r_b = Raum_Belegung.get.filter(raum=raum)
                            aktuelle_ag = r_b.ag.name
            
            ogs_groups = Gruppe.objects.all()

            return render(request, "pupil/pupil.html", {"schueler":schueler, "nutzer":nutzer, "bus_kind":bus_kind, "aufenthalt":aufenthalt, "aktuelle_ag":aktuelle_ag, "ogs_groups":ogs_groups})
        
    return redirect("master_web")