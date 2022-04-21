from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'itineraires'
urlpatterns = [
    path('', login_required(
        views.ItinerairesView.as_view(
            template_name='itineraires/itineraires.html')),
         name='itineraires'),
    
    path('sorties/<int:itineraire_id>',
         views.sorties,
         name="sorties")
]