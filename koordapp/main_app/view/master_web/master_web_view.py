from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Personal

def master_web_view(request):
    if request.user.is_authenticated:
        return render(request, 'master_overview/master_web.html')
    else:
        return redirect("login")