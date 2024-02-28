from django.shortcuts import render
from .models import Place, Port  # Import both models in one line



def myfun(request):
    obj = Place.objects.all()
    pot = Port.objects.all()
    return render(request, "index.html", {'res': obj, 'team': pot})

