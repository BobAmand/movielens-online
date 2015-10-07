from django.db import models
#from django.contrib.auth.models import Rater

# Create your models here.

class Rater(models.Model):
    # id is automatic
    age = models.IntegerField(default=0)
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return.id

class Movie(models.Model):
    class Meta:
        verbose_name_plural = 'movies'
    movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    # release_date = models.DateField()
    # video_release_date = models.DateField()
    # IMDB_URL = models.URLField(max_length=100)
    # # unknown =
    # action = models.BooleanField()
    # adventure = models.BooleanField()
    # animation = models.BooleanField()
    # children_s = models.BooleanField()
    # comedy = models.BooleanField()
    # crime = models.BooleanField()
    # documentary = models.BooleanField()
    # drama = models.BooleanField()
    # fantasy = models.BooleanField()
    # film_noir = models.BooleanField()
    # horror = models.BooleanField()
    # musical = models.BooleanField()
    # mystery = models.BooleanField()
    # romance = models.BooleanField()
    # sci_fi = models.BooleanField()
    # thriller = models.BooleanField()
    # war = models.BooleanField()
    # western = models.BooleanField()
    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('rating'))['rating__avg']

    def __str__(self):
        self.title

class Rating(models.Model):
    class Meta:
        verbose_name_plural = 'ratings'
    user_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()
    #time_stamp = models.DateTimeField()

    def __str__(self):
        return 'user {} gives {} a {} stars'.format(self.user_id, self.item_id, self.rating)
