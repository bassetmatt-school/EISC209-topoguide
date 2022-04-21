from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import time

class Itineraire(models.Model) :
    #Main info
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    start_point = models.CharField(max_length=100)
    
    #Height info
    base_height = models.IntegerField(default=0)
    min_height = models.IntegerField(default=0)
    max_height = models.IntegerField(default=0)
    
    #Cumulated elevation elevation gains
    pos_elev_gain = models.IntegerField(default=0)
    neg_elev_gain = models.IntegerField(default=0)
    
    #Using a timedelta object for intuitive fields for duration
    estim_duration = models.TimeField(default=time(hour=1))
    #Ensures the difficulty is between 1 and 5
    estim_difficulty = models.IntegerField(
        default=1, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    
    def __str__(self) :
        return self.title
    
    def time_formatted(self) :
        s = ""
        if self.estim_duration.hour > 0 :
            s+= f"{self.estim_duration.hour:2d}h"
            if self.estim_duration.minute > 0 :
                s += f"{self.estim_duration.minute:02d}"
        elif self.estim_duration.minute > 0 :
            s+= f"{self.estim_duration.minute:2d} min"
        return s
class Sortie(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    route = models.ForeignKey(Itineraire, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    actual_duration = models.TimeField(default=time(hour=1))
    number_people = models.IntegerField(default=1)
    
    XP_LEVEL = [
        ('B', "Beginners"),
        ('E', "Experienced"),
        ('M', "Mixed"),
    ]
    
    group_xp = models.CharField(
        choices = XP_LEVEL,
        max_length = 1,
        default = 'B'
    )
    
    WEATHER_TYPES = [
        ('G', "Good"),
        ('N', "Neutral"),
        ('B', "Bad"),
    ]
    
    weather = models.CharField(
        choices = WEATHER_TYPES,
        max_length = 1,
        default = 'N'
    )
    
    #Ensures the difficulty is between 1 and 5
    difficulty_felt = models.IntegerField(
        default = 1, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    def __str__(self) :
        return f"{self.route} by {self.user}"