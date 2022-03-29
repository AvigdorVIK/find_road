from django.shortcuts import render

from cities.models import City


def home (request):
    qs = City.objects.all()
    context = {'list_name': qs}


    return render (request, 'cities/home.html', context)
