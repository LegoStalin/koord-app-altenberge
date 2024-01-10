from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Personal

def room_history_view(request):
    return render(request, 'history_pages/room_usage_history.html')