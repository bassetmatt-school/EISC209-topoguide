from django.urls import path

from . import views

app_name = 'itineraires'
urlpatterns = [
    path('', views.ItinerairesView.as_view(), name='itineraires'),
]