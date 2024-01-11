from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Raum_Belegung, Aufenthalt, Nutzer, Schueler, Zeitraum, Raum_Historie
from datetime import datetime

def room_history_view(request, pupil):
    if(Nutzer.objects.filter(id=pupil).exists):
        nutzer = Nutzer.objects.get(id=pupil)
        if(Schueler.objects.filter(user_id=nutzer).exists):
            schueler = Schueler.objects.get(user_id=nutzer)
            aufenthalte = Aufenthalt.objects.filter(schueler_id = schueler)
            hist = []
            for aufenthalt in aufenthalte:
                zeitraum = aufenthalt.zeitraum
                startzeit = zeitraum.startzeit
                endzeit = zeitraum.endzeit
                raum = aufenthalt.raum_id
                kategorie = "Gruppenraum"
                raum_historie = None
                if not endzeit == None:
                    endzeit = endzeit.strftime("%H:%M")
                    if(Raum_Historie.objects.filter(raum=raum,zeitraum__startzeit__lt=startzeit,zeitraum__endzeit__gte=endzeit).exists()):
                        raum_historie = Raum_Historie.objects.get(raum=raum,zeitraum__startzeit__lt=startzeit,zeitraum__endzeit__gte=endzeit)
                        if not raum_historie.ag_kategorie == None:
                            kategorie = raum_historie.ag_kategorie.name
                elif(Raum_Belegung.objects.filter(raum=raum).exists()):
                    r_b = Raum_Belegung.objects.get(raum=raum)
                    endzeit = "In Benutzung"
                    if not r_b.ag.ag_kategorie == None:
                        kategorie = r_b.ag.ag_kategorie.name
                
                
                history = History(date=datetime.now().date().strftime("%d.%m.%Y"),start_time=startzeit.strftime("%H:%M"),end_time=endzeit,kategorie=kategorie,raum=raum)
                hist.append(history)
            return render(request, 'history_pages/room_history.html', {"historys":hist,"user":nutzer})
    return redirect("master_web")

class History:
    def __init__(self, date, start_time, end_time, kategorie, raum):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.kategorie = kategorie
        self.raum = raum