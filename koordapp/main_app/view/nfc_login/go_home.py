from django.shortcuts import redirect, render
from main_app.models import Nutzer, Feedback, Schueler
from datetime import datetime

def go_home_view(request, feedback=None):
    tag_id = request.session.get('tag_id', None)
    if not tag_id == None:
        if(Nutzer.objects.filter(tag_id=tag_id).exists()):
            nutzer = Nutzer.objects.get(tag_id=tag_id)
            if not feedback == None:
                try:
                    feedback = Feedback.Feedbacks[feedback.upper()].value
                except KeyError:
                    return redirect("home")
                if(Schueler.objects.filter(user_id=nutzer).exists()):
                    schueler = Schueler.objects.get(user_id=nutzer)
                    feedback = Feedback.objects.create(feedback_wert = feedback, schueler_id = schueler, tag = datetime.now().date())
                    print("Feedback für " + nutzer.vorname + " wurde gesetzt: " + feedback.feedback_wert)     #Debugging
                    request.session['tag_id'] = None
                    redirect("home")
            else:
                return render(request, 'checked_out/checked_out.html', {"nutzer":nutzer})
    return redirect("home")