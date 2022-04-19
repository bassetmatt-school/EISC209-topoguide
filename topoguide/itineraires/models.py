from django.db import models
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
class Itineraire(models.Model) :
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    start_point = models.CharField(max_length=100)
    
    base_height = models.IntegerField(default=0)
    min_height = models.IntegerField(default=0)
    max_height = models.IntegerField(default=0)
    
    pos_elev_gain = models.IntegerField(default=0)
    neg_elev_gain = models.IntegerField(default=0)
    
    estim_duration = models.DurationField(default=timedelta(hours=1))
    estim_difficulty = models.IntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    
    def __str__(self) :
        return self.title