from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Personal, Gruppe

def master_web_view(request):
    if request.user.is_authenticated:
        user = request.user
        has_ogs = False
        if(Personal.objects.filter(user=user).exists()):
            personal = Personal.objects.get(user=user)
            if(Gruppe.objects.filter(gruppen_leiter=personal).exists()):
                has_ogs = True
        return render(request, 'master_overview/master_web.html', {"user":user, "has_ogs":has_ogs})
    else:
        return redirect("login")