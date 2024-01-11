from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from main_app.models import Raum_Belegung, Aufenthalt, Nutzer, Schueler, Zeitraum
from datetime import datetime

def home_view(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        tag_id = request.POST.get('tag_id')
        device_id = request.COOKIES.get('device_id')
        if(Raum_Belegung.objects.filter(tablet_id=device_id).exists()):
            r_b = Raum_Belegung.objects.get(tablet_id=device_id)
            raum = r_b.raum
            request.session['tag_id'] = tag_id
            if(Aufenthalt.objects.filter(raum_id=raum, schueler_id__user_id__tag_id=tag_id, zeitraum__endzeit__isnull=True).exists()):
                return redirect("leave_room")
            else:
                if(Nutzer.objects.filter(tag_id=tag_id).exists()):
                    nutzer = Nutzer.objects.get(tag_id=tag_id)
                    if(Schueler.objects.filter(user_id=nutzer).exists()):
                        schueler = Schueler.objects.get(user_id=nutzer)
                        if(schueler.angemeldet == False):
                            schueler.angemeldet = True
                            schueler.save()
                        zeitraum = Zeitraum.objects.create(startzeit = datetime.now().time(), endzeit = None)
                        Aufenthalt.objects.create(raum_id=raum, zeitraum=zeitraum, schueler_id=schueler, tag=datetime.now().date())
                        return redirect('checked_in')
    return render(request,"home/home.html")
