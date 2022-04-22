from django.contrib import admin

from .models import Itineraire, Sortie

# Access to the models for the admin users to modify or create them
admin.site.register(Itineraire)
admin.site.register(Sortie)