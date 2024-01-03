from django.shortcuts import render
from models import Schueler

def search_pupil(request):
    results = None

    if request.method == 'POST':
        search_query = request.POST.get('Search', '')
        results = Schueler.objects.filter(name_eb__icontains=search_query)

    return render(request, 'search_pupil.html', {'results': results})