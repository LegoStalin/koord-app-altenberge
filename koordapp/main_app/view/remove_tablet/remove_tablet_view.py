from django.shortcuts import redirect, render
from main_app.models import Raum_Belegung
def remove_tablet_view(request):
    if request.method == 'POST':
        if 'submit_rr' in request.POST:
            device_id = request.COOKIES.get('device_id')
            if(Raum_Belegung.objects.filter(tablet_id=device_id).exists()):
                raum_belegung = Raum_Belegung.objects.get(tablet_id=device_id)
                raum_belegung.delete()
                return redirect('choose_room')
        elif 'abort_rr' in request.POST:
            return redirect('master_tablet')
    return render(request, "master_android/remove_tablet.html")