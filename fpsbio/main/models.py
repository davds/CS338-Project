from django.db import models
from datetime import datetime   
#from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Profile(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.tutorial_title

#class Profile(models.Model):
    #profile_username = models.TextField()
    #profile_name = models.TextField()
    #profile_age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    #profile_card_info = ArrayField(models.CharField(max_length=20), blank=True)
    
    #def __str__(self):
    #    return self.profile_username