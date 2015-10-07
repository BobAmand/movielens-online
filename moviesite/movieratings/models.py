from django.db import models
#from django.contrib.auth.models import Rater

# Create your models here.

class Rater(models.Model):
    age = models.IntegerField(default=0)
    # gender = models.CharField(max_length=1)
    occupation = models.IntegerField(default=0)
    zip_code = models.PositiveSmallIntegerField(default=0)

class Movie(models.Model):
    class Meta:
        verbose_name_plural = 'movies'
    movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=60)
    release_date = models.DateField()
    video_release_date = models.DateField()
    IMDB_URL = models.URLField(max_length=100)
    # unknown =
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    children_s = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

class Rating(models.Model):
    class Meta:
        verbose_name_plural = 'ratings'
    user_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    time_stamp = models.DateTimeField()
