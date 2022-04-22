from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Itineraire, Sortie

class IndexView(generic.ListView):
    template_name = 'itineraires/itineraires.html'
    context_object_name = 'route_list'
    
    def get_queryset(self):
        return Itineraire.objects.order_by('title')

class RouteDetailView(generic.DetailView) :
    model = Itineraire
    template_name = "itineraires/sorties.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Gets the route
        route = self.get_object()
        context['route'] = route
        # Gets all trips on this route
        context['trip_list'] = Sortie.objects.all().filter(route=route)
        return context

class TripDetailView(generic.DetailView) :
    model = Sortie
    template_name = 'itineraires/sortie.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Gets the trip
        trip = self.get_object()
        context['trip'] = trip
        # Gets the route of the trip for more lisibility
        context['route'] = trip.route
        return context

class TripCreateView(generic.CreateView):
    model = Sortie 
    fields = ['date','actual_duration','number_people','group_xp','weather','difficulty_felt']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True
        return context
    
    def get_success_url(self):
        return reverse('itin:detail_trip', kwargs={'trip_id': self.object.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.route = Itineraire.objects.get(id=self.request.GET.get("route_id"))
        return super().form_valid(form)

class TripUpdateView(generic.UpdateView):
    model = Sortie
    fields = ['date','actual_duration','number_people','group_xp','weather','difficulty_felt']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = False
        return context
    
    def get_success_url(self):
        return reverse('itin:detail_trip', kwargs={'trip_id': self.object.pk})
    
    def form_valid(self, form):
        if form.instance.user == self.request.user :
            return super().form_valid(form)
        else :
            return HttpResponseForbidden("You aren't the creator of this trip, you can't edit it")