from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'it'
urlpatterns = [
    path(
        'itineraires/', 
        name = 'index',
        view = login_required(
            views.IndexView.as_view()
        )
    ),
    
    path(
        'sorties/<int:route_id>',
        name="detail",
        view = login_required(
            views.sorties
        ),
    ),
    
    path(
        'sortie/<int:trip_id>',
        name="sortie_view",
        view = login_required(
            views.sortie
        )
    ),
    
    path(
        'nouvelle_sortie/',
        name = "new_trip",
        view = login_required(
            views.TripCreateView.as_view()
        )
    ),
    
    path(
        'modif_sortie/<int:pk>',
        name = "edit_trip",
        view = login_required(
            views.TripUpdateView.as_view()
        )
    )
]