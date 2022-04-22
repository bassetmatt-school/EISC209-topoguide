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
        'sorties/<int:itineraire_id>',
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
    )
]