from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Raum, Raum_Historie, Aufenthalt
from datetime import datetime

@login_required(login_url="login")
def room_usage_history_view(request, raum):
    if(Raum.objects.filter(raum_nr=raum).exists):
        raum = Raum.objects.get(raum_nr=raum)
        raum_historien = Raum_Historie.objects.filter(raum=raum)
        list_histories = []
        for raum_historie in raum_historien:
            date = raum_historie.tag.strftime("%d-%m-%Y")
            time = raum_historie.zeitraum.startzeit.strftime("%H:%M") + " - " + raum_historie.zeitraum.endzeit.strftime("%H:%M")
            number=0
            alle_schueler_im_raum = Aufenthalt.objects.filter(raum_id=raum)
            for schueler_in_raum in alle_schueler_im_raum:
                if raum_historie.zeitraum.startzeit < schueler_in_raum.zeitraum.startzeit:
                    if schueler_in_raum.zeitraum.endzeit == None or schueler_in_raum.zeitraum.endzeit <= raum_historie.zeitraum.endzeit:
                        number += 1
            history = History(date, time, number)
            list_histories.append(history)
        return render(request, 'history_pages/room_usage_history.html', {"historien":list_histories,"raum":raum})
    return redirect('master_web')

class History:
    def __init__(self, date, time, number):
        self.date = date
        self.time = time
        self.number = number