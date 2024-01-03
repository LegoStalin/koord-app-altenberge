from django.shortcuts import render
from models import Schueler

def search_pupil(request):
    schueler_list = Schueler.objects.all() #alle schüler in einer Liste speichern 
    if 'selected_schueler' in request.GET: # if methode um zu schauen ob ein schueler ausgewählt wurde
        selected_schueler_id = request.GET['selected_schueler'] #bekommt selected_schueler
        selected_schueler = get_object_or_404(Schueler, id= selected_schueler_id) #get_ob.. ist eig nen shortcut für nh 404 exception wenn die ID nicht gefunden wurde
        current_room = selected_schueler.gruppen_id.raum if selected_schueler.gruppen_id else None #bekommt assozierte gruppe des schuelers und bekommt das raum attribut. Wen der schueler nicht in einer gruppe ist, wird es auf None gesetzt
    else: 
        selected_schueler = None
        current_room = None
    return render(request, 'search_pupil.html', {'schueler_list': schueler_list, 'selected_schueler': selected_schueler, 'current_room' : current_room})

    if request.method == 'POST':
        search_query = request.POST.get('Search', '')
        results = Schueler.objects.filter(name_eb__icontains=search_query)
        return render(request, 'search_pupil.html', {'schueler_list': schueler_list, 'selected_schueler': selected_schueler, 'current_room':current_room, 'results': results})
    return render(request, 'search_pupil.html', {'schueler_list': schueler_list, 'selected_schueler': selected_schueler, 'current_room': current_room})