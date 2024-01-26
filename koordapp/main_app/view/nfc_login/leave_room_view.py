from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Aufenthalt, Raum_Belegung, Nutzer, Schueler, Personal, Raum_Belegung
from datetime import datetime
from main_app.view.remove_tablet.remove_tablet_view import remove_tablet

def leave_room_view(request):
    if not request.session.get('tag_id', None) == None:
        tag_id = request.session.get('tag_id', None)
        device_id = request.COOKIES.get('device_id')
        r_b = Raum_Belegung.objects.get(tablet_id=device_id)
        raum = r_b.raum
        if(Aufenthalt.objects.filter(raum_id=raum, schueler_id__user_id__tag_id=tag_id, zeitraum__endzeit__isnull=True).exists()): # ist abgemeldeter Nutzer wirklich im Raum?
            if request.method == 'POST':
                if(Nutzer.objects.filter(tag_id=tag_id)):
                    nutzer = Nutzer.objects.get(tag_id = tag_id)
                    if(Schueler.objects.filter(user_id=nutzer).exists()):
                        schueler = Schueler.objects.get(user_id=nutzer)
                        aufenthalt = Aufenthalt.objects.get(raum_id=raum, schueler_id__user_id__tag_id=tag_id, zeitraum__endzeit__isnull=True)
                        zeitraum = aufenthalt.zeitraum
                        zeitraum.endzeit = datetime.now().time()
                        zeitraum.save()
                        if('button_leave_room' in request.POST):   
                            return redirect('checked_out')
                        elif('button_leave_school' in request.POST):
                            schueler.angemeldet = False
                            schueler.save()
                            return redirect('go_home')
                        
                    elif(Personal.objects.filter(user=nutzer).exists()):
                        personal = Personal.objects.get(user=nutzer)
                        if(Raum_Belegung.objects.filter(aufsichtsperson=personal).exists()):
                            r_b = Raum_Belegung.objects.get(aufsichtsperson=personal)
                            return remove_tablet(request, r_b.tablet_id)
                return redirect("home")
            return render(request, 'room_plan/room_overview.html')
        else:
            return redirect("checked_in")
    return redirect("home")