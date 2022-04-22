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
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context
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

class TripUpdateView(generic.UpdateView):
    model = Sortie
    fields = ['date','actual_duration','number_people','group_xp','weather','difficulty_felt']

    def get_success_url(self):
        return reverse('it:sortie_view', kwargs={'trip_id': self.object.pk})
    
    def form_valid(self, form):
        if form.instance.user == self.request.user :
            return super().form_valid(form)
        else :
            return HttpResponseForbidden("You aren't the creator of this trip, you can't edit it")