from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import time

def time_format(t : time) -> str:
    """Small function that parses the time for a nice looking result

    Args:
        t (time): the time to be parsed, type datetime.time

    Returns:
        str : The corresponding string 
    """
    s = ""
    if t.hour > 0 :
        s+= f"{t.hour:2d}h"
        if t.minute > 0 :
            s += f"{t.minute:02d}"
    elif t.minute > 0 :
        s+= f"{t.minute:2d} min"
    else :
        s+= "Instantané"
    return s

class Itineraire(models.Model) :
    """Class that represent a route

    Attributes :
        title (models.CharField) : The title of the route
        description (models.TextField) : A text that describes the route
        start_point (models.CharField) : The start point of the route
        base_height (models.IntegerField) : The height of the starting point
        min_height (models.IntegerField) : The minimal height during the route
        max_height (models.IntegerField) : The maximal height during the route
        pos_elev_gain (models.IntegerField) : The cumulated positive 
        elevation gain
        neg_elev_gain (models.IntegerField) : The cumulated negative 
        elevation gain
        estim_duration (models.TimeField) : The estimated duration of the 
        route
        estim_difficulty (models.IntegerField) : The estimated difficulty of
        the route from 1 to 5
    """
    #Main info
    title = models.CharField("Nom de l'itinéraire",max_length=50)
    description = models.TextField("Description",max_length=1000)
    start_point = models.CharField("Point de départ",max_length=100)
    
    #Height info
    base_height = models.IntegerField("Altitude de départ",default=0)
    min_height = models.IntegerField("Altitude minimale",default=0)
    max_height = models.IntegerField("Altitude maximale",default=0)
    
    #Cumulated elevation elevation gains
    pos_elev_gain = models.IntegerField("Dénivelé cumulé positif",default=0)
    neg_elev_gain = models.IntegerField("Dénivelé cumulé négatif",default=0)
    
    #Using a timefield for intuitive fields for duration
    estim_duration = models.TimeField("Durée estimée",default=time(hour=1))
    #Ensures the difficulty is between 1 and 5
    estim_difficulty = models.IntegerField(
        "Difficulté estimée",
        default=1, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    
    def __str__(self) :
        return self.title
    
    def time_display(self) :
        """Time formatting"""
        return time_format(self.estim_duration)
    
class Sortie(models.Model) :
    """Class that reprensents a trip on a given route

    Attributes :
        user = (models.ForeignKey(User)) : The user that created this trip
        route = (models.ForeignKey(Itineraire)) : The route taken by the user
        date (models.DateField) : The date of the trip
        actual_duration (models.TimeField) : The actual duration of the trip
        number_people (models.IntegerField) : The number of people that were doing the trip 
        group_xp (models.CharField) : The experience level of the group
        weather (models.CharField) : The weather conditions the day of the trip
        difficulty_felt (models.IntegerField) : The difficulty perceived by the group
    """
    class xp_level(models.TextChoices):
        BEGINNERS   = 'B', ('Tous débutants')
        EXPERIENCED = 'E', ('Tous expérimentés')
        MIXED       = 'M', ('Mixte')
        
    class weather_type(models.TextChoices):
        GOOD    = 'G', ('Bonnes')
        NEUTRAL = 'N', ('Moyennes')
        BAD     = 'B', ('Mauvaises')
        
    user = models.ForeignKey(User,verbose_name="Utilisateur",on_delete=models.CASCADE)
    route = models.ForeignKey(Itineraire,verbose_name="Itinéraire", on_delete=models.CASCADE)
    date = models.DateField("Date de la sortie",default=timezone.now)
    actual_duration = models.TimeField("Durée réelle",default=time(hour=1))
    number_people = models.IntegerField(
        "Nombre de participants",
        default=1,
        validators=[
            MinValueValidator(1)
        ]
        )
    
    group_xp = models.CharField(
        "Expérience du groupe",
        max_length = 1,
        choices=xp_level.choices,
        default=xp_level.BEGINNERS,
    )
    
    weather = models.CharField(
        "Conditions météo",
        max_length = 1,
        choices=weather_type.choices,
        default=weather_type.GOOD,
    )
    
    #Ensures the difficulty is between 1 and 5
    difficulty_felt = models.IntegerField(
        "Difficulté ressentie",
        default = 1, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

            
    def __str__(self) :
        return f"{self.route} by {self.user}"
    
    def time_display(self) :
        """Time formatting"""
        return time_format(self.actual_duration)