from django.shortcuts import redirect, render

def ogs_group_view(request):
    return render(request, "ogs_group/ogs_group.html")