from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Personal, Raum, Gruppe, Schueler
from django.contrib.auth.models import User

@login_required(redirect_field_name="login")
def ogs_group_view(request):

    user = request.user
    search = ''
    if(Personal.objects.filter(user=user).exists()):
        personal = Personal.objects.get(user=user)
        if(Gruppe.objects.filter(gruppen_leiter=personal).exists()):
            gruppe = Gruppe.objects.get(gruppen_leiter=personal)
            schueler = Schueler.objects.filter(gruppen_id=gruppe)
            if request.method == 'POST':
                search = request.POST.get('search')
                if 'button_search' in request.POST:
                    schueler2 = []
                    for schueler1 in schueler:
                        name = schueler1.user_id.vorname + " " + schueler1.user_id.nachname
                        if(search in name):
                            schueler2.append(schueler1)
                    schueler = schueler2
        else:
            #fehler Nachricht?
            return redirect("master_web")  
    else:
        #fehler Nachricht?
        return redirect("master_web")

    return render(request, "ogs_group/ogs_group.html",{"schueler":schueler, "search":search, "group_name":gruppe.name})