from django.db import models

# Create your models here.
'''
Three models are contained to control
   Rater = the individual rating the movie.
   Movie = the movie title.
   Rating = links the rater and movie by star rating.

Id assumed by Django; rater_id needs to be a string.
'''
class Rater(models.Model):   #simplified models

    MALE = 'M'   # Constants for controlled entry
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    GENDER_SELECT = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'No Data')
    )

    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_SELECT, null=True)
    occupation = models.IntegerField(default=0)
    zipcode = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.id)

class Movie(models.Model):

    class Meta:
        verbose_name_plural = 'movies'

    title = models.CharField(max_length=255, null=True)
        # minimized the list of data available; genria is in View Git

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']
        # 'stars__avg' is dynamically calculating the average.

    def num_rating(self):
        return self.rating_set.aggregate(models.Count('citizen'))['citizen__count']
        # attempt to determine how many raters occurred per movie.


    def __str__(self):
        return self.title

class Rating(models.Model):

    class Meta:
        verbose_name_plural = 'ratings'

    citizen = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveIntegerField()

    def __str__(self):
        return 'User {} rates {} with {} stars.'.format(self.citizen, self.movie, self.stars)

'''
The 'fixtures' dir established as a parking space for the .json files.
The 'fixtures' dir is just below the App and at same level as 'migrations'
'''

def load_raters_dat():
    import csv
    import json

    citizens = []
    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=
                                'UserID::Gender::Age::Occupation::Zip-code'.
                                split('::'),
                                delimiter='\t')

        for row in reader:
            citizen = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code']
                },
                'model': 'movieapp.Rater',
                'pk': int(row['UserID']),
            }
            citizens.append(citizen)
            # appends citizen data to citizens list as a dict.
            # following writes the citizens dict into a json file.
    with open('movieapp/fixtures/rater.json', 'w') as f:
        f.write(json.dumps(citizens))
            # the 'w' in open will overwrite the data at function run.

def load_movies_dat():
    import csv
    import json
                    # added encoding "Windows-1252" to overcome
                    # a UnicodedDecodeError: 'utf-8'
    movies = []
    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=
                                'MovieID::Title::Genres'.split('::'),
                                delimiter='\t')

        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title']
                },
                'model': 'movieapp.Movie',
                'pk': int(row['MovieID']),
            }
            movies.append(movie)
            # appends movie data to movies list as a dict
            # following writes the movies dict into a json file.
    with open('movieapp/fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))


def load_ratings_dat():
    import csv
    import json

    ratings = []
    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=
                                'UserID::MovieID::Rating::Timestamp'.
                                split('::'),
                                delimiter='\t')

        for row in reader:
            rating = {
                'fields': {
                    'citizen': row['UserID'],
                    'movie': row['MovieID'],
                    'stars': row['Rating']
                },
                'model': 'movieapp.Rating',
            }
            ratings.append(rating)
            # appends rating data to ratings list as a dict
            # following writes the ratings dict into a json file
    with open('movieapp/fixtures/stars.json', 'w') as f:
        f.write(json.dumps(ratings))


def load_dat_data():
    load_raters_dat()
    print("Raters data has been loaded as json to fixtures dir.")
    load_movies_dat()
    print("Movies data has been loaded as json to fixtures dir.")
    load_ratings_dat()
    print("Ratings data has been loaded as json to fixtures dir.")
