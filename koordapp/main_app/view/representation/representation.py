from django.shortcuts import render

def representation_view(request):
    return render(request, 'representation/representation.html')