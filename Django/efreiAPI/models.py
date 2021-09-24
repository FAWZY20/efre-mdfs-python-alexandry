from django.db import models

# Create your models here.
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantite = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
