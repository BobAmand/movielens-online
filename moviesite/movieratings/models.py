from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Rater(models.Model):
    # age = models.integer
    occupation = models.CharField(max_length=10)

class Movies(models.Model):
    pass

class Ratings(models.Model):
    pass
