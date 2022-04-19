from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Itineraire
from django.template import loader


def itineraires(request):
    route_list = Itineraire.objects.order_by('title')
    context = {
        'route_list' : route_list   
    }
    return render(request, 'itineraires/itineraires.html', context )