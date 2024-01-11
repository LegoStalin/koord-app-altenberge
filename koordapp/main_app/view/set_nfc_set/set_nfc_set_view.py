from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from main_app.models import Nutzer, Personal, Schueler
from itertools import chain

@login_required(redirect_field_name="login")
def set_nfc_set_view(request, id):
    schueler = Schueler.objects.all()
    users = [s.user_id for s in schueler]
    if request.user.is_superuser:
        personal = Personal.objects.all()
        personal_users = [p.nutzer for p in personal]
        users = list(chain(users, personal_users))
    tag_username = "Niemand"
    nutzer = None
    if(Nutzer.objects.filter(tag_id=id).exists()):
        nutzer = Nutzer.objects.get(tag_id=id)
        tag_username = nutzer.vorname + " " + nutzer.nachname
    if request.method == 'POST':
        search = request.POST.get('search')
        if 'button_search' in request.POST:
            users2 = []
            for user in users:
                name = user.vorname + " " + user.nachname
                if(search.lower() in name.lower()):
                    users2.append(user)
            users = users2
        if 'button_change_tag' in request.POST:
            new_tag_owner_id = request.POST.get('button_change_tag')
            if not nutzer == None:
                nutzer.tag_id = None
                nutzer.save()
            if Nutzer.objects.filter(id=new_tag_owner_id).exists():
                new_nutzer = Nutzer.objects.get(id=new_tag_owner_id)
                tag_username = new_nutzer.vorname + " " + new_nutzer.nachname
                new_nutzer.tag_id = id
                new_nutzer.save()
            else:
                return redirect(request.path)
    return render(request, 'set_nfc_set/set_nfc_set.html', {"id":id, "users":users, "tag_username":tag_username})