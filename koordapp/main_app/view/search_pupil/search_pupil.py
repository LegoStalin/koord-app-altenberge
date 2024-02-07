from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Aufenthalt, Personal, Raum_Belegung, Schueler
from django.db.models import Q

@login_required(login_url="login")
def search_pupil_view(request):
    user = request.user
    personal = Personal.objects.get(user=user)
    raumbelegungen = Raum_Belegung.objects.filter(
    Q(aufsichtspersonen=personal) &
    Q(zeitraum__endzeit__isnull=True))
    raeume = [belegung.raum.id for belegung in raumbelegungen]
    aufenthalte = Aufenthalt.objects.filter(Q(raum_id__id__in=raeume) & Q(zeitraum__endzeit__isnull=True))
    schueler = [aufenthalt.schueler_id for aufenthalt in aufenthalte]
    if request.method == 'POST':
        search = request.POST.get('search')
        if 'button_search' in request.POST:
            schueler2 = []
            for schueler1 in schueler:
                name = schueler1.user_id.vorname + " " + schueler1.user_id.nachname
                if(search.lower() in name.lower()):
                    schueler2.append(schueler1)
            schueler = schueler2
    schueler = sorted(schueler, key=lambda schueler: (schueler.user_id.vorname, schueler.user_id.nachname))
    return render(request, "search_pupil/search_pupil.html", {"schueler":schueler})