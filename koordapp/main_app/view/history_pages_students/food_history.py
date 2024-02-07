from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main_app.models import Raum_Belegung, Aufenthalt, Nutzer, Schueler, Zeitraum, Feedback
from datetime import datetime

@login_required(redirect_field_name="login")
def food_history_view(request, pupil):
    if(Nutzer.objects.filter(id=pupil).exists()):
        nutzer = Nutzer.objects.get(id=pupil)
        if(Schueler.objects.filter(user_id=nutzer).exists()):
            schueler = Schueler.objects.get(user_id=nutzer)
            feedbacks = Feedback.objects.filter(schueler_id=schueler, mensa_feedback=True)
            
            # get list if dates for the last to weeks
            # lookup feedbacks contains an element where feedback.tag == date

    return render(request, "history_pages/food_history.html", {'pupil':pupil})