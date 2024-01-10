from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Personal

def leave_room_view(request):
    if not request.session.get('tag_id', None) == None:
        device_id = request.COOKIES.get('device_id')
    
    return redirect("home")