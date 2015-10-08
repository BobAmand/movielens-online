from django.db import models
#from django.contrib.auth.models import Rater

# Create your models here.

class Rater(models.Model):
    # id is automatic
    age = models.PositiveIntegerField()

    MALE = 'M'       # Establishing constants to control entry.
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'Did not answer')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    occupation = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.id)

class Movie(models.Model):
    class Meta:
        verbose_name_plural = 'movies'
    #movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=255, null=True)
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
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']
        # 'stars__avg' is dynamically calculating the average.

    def __str__(self):
        return self.title

class Rating(models.Model):
    class Meta:
        verbose_name_plural = 'ratings'
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveSmallIntegerField()
    #time_stamp = models.DateTimeField()

    def __str__(self):
        return 'User {} rates {} with {} stars.'.format(self.user, self.movie, self.stars)


def load_ml_data():
    import csv
    import json
    import re

    users = []
    with open('ml-1m/users.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'movieratings.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)
#need movie
#need rater
