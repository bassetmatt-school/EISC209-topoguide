from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Itineraire, Sortie

class IndexView(generic.ListView):
    template_name = 'itineraires/itineraires.html'
    context_object_name = 'route_list'
    
    def get_queryset(self):
        return Itineraire.objects.order_by('title')

def sorties(request, route_id):
    route = get_object_or_404(Itineraire,pk=route_id)
    trip_list = Sortie.objects.all().filter(route=route)
    context = {
        'route' : route,
        'trip_list' : trip_list
    }
    return render(request,
                  'itineraires/sorties.html',
                  context)

"""
class DetailView(generic.DetailView):
    model = Itineraire
    album = get_object_or_404(Sortie, pk=model.id)
""" 

def sortie(request, trip_id):
    trip = get_object_or_404(Sortie,pk=trip_id)
    route = trip.route
    context = {
        'trip' : trip,
        'route' : route
    }
    return render(request,
                  'itineraires/sortie.html',
                  context)

class TripCreateView(generic.CreateView):
    model = Sortie
    fields = ['date','actual_duration','number_people','group_xp','weather','difficulty_felt']
    
    def get_success_url(self):
        return reverse('it:sortie_view', kwargs={'trip_id': self.object.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.route = Itineraire.objects.get(id=self.request.GET.get("route_id"))
        return super().form_valid(form)