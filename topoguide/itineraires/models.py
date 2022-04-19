from django.db import models
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator

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
    estim_duration = models.DurationField(default=timedelta(hours=1))
    #Ensures the difficulty is between 1 and 5
    estim_difficulty = models.IntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    
    def __str__(self) :
        return self.title