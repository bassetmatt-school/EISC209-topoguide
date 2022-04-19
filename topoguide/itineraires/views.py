from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Itineraire
from django.template import loader

class ItinerairesView(generic.ListView):
    template_name = 'itineraires/itineraires.html'
    context_object_name = 'route_list'
    
    def get_queryset(self):
        return Itineraire.objects.order_by('title')