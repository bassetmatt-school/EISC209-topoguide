from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'itineraires'
urlpatterns = [
    path(
        'itineraires/', 
        name = 'itineraires',
        view = login_required(
            views.IndexView.as_view()
        )
    ),
    
    path(
        'sorties/<int:itineraire_id>',
        name="sorties",
        view = login_required(
            views.sorties
        ),
    )
]