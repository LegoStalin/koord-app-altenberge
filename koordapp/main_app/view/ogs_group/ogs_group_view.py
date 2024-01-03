from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Personal, Raum, Gruppe, Schueler
from django.contrib.auth.models import User

@login_required(login_url="login/")
def ogs_group_view(request, gruppe):

    if Gruppe.objects.filter(name=gruppe).exists():
        gruppe = Gruppe.objects.get(name=gruppe)
        schueler = Schueler.objects.filter(gruppen_id=gruppe)
        user = request.user
        personal = Personal.objects.get(user=user)
        if not Personal == None:
            if gruppe.gruppenleiter_leiter == personal:
                pass
            else:
                #fehler Nachricht?
                return redirect("master_web")
        else:
            pass
    else:
        #fehler Nachricht?
        return redirect("master_web")

    return render(request, "ogs_group/ogs_group.html",{"schueler":schueler})