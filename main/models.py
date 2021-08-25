from django.db import models
from datetime import datetime   
#from django.core.validators import MinValueValidator, MaxValueValidator

class CardItem(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    def __str__(self):
        return self.key + "_" + str(self.id)

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200,default="game")
    items = models.ManyToManyField(CardItem, blank=True)
    content = models.CharField(max_length=99999,blank=True,default="")
    def __str__(self):
        return self.title + "_" + str(self.id)

class Profile(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200,blank=True)
    image = models.CharField(max_length=200,blank=True)
    theme = models.CharField(max_length=200,blank=True)
    content = models.TextField()
    last_updated = models.DateTimeField('date published', default=datetime.now)
    cards = models.ManyToManyField(Card, blank=True)
    def __str__(self):
        return self.username