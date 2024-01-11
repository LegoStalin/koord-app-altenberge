from django.shortcuts import redirect, render
from main_app.models import Nutzer

def checked_in_view(request):
    tag_id = request.session.get('tag_id', None)
    if not tag_id == None:
        if(Nutzer.objects.filter(tag_id=tag_id).exists()):
            nutzer = Nutzer.objects.get(tag_id=tag_id)
            request.session['tag_id'] = None
            return render(request,'checked_in/checked_in.html', {"nutzer":nutzer})
    return redirect("home")