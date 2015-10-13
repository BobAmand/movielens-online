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
    zipcode = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):

    class Meta:
        verbose_name_plural = 'movies'
    # movie_id = models.PositiveIntegerField(default=0)
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
    movie = models.ForeignKey(Movie) #trace the movie vs movieID
    stars = models.PositiveSmallIntegerField()
    #time_stamp = models.DateTimeField()

    def __str__(self):
        return 'User {} rates {} with {} stars.'.format(self.user, self.movie, self.stars)


def load_ml_users():
    import csv
    import json

    users = []
    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
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

    with open('movieratings/fixtures/users.json', 'w') as f:
        f.write(json.dumps(users))

def load_ml_movies():
    import csv
    import json

    movies = []
    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    # 'movie_id': row['MovieID'],
                    'title': row['Title']
                },
                'model': 'movieratings.Movie',
                'pk': int(row['MovieID']),
            }
            movies.append(movie)

    with open('movieratings/fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))

def load_ml_ratings():
    import csv
    import json

    count = 1
    ratings = []
    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::aMovieID::Rating::Timestamp'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            print("reading row {}".format(count))
            rating = {
                'fields': {
                    'user': row['UserID'],
                    'movie': row['aMovieID'],  #refers to fieldnames
                    'stars': row['Rating']
                },
                'model': 'movieratings.Rating',
            }
            ratings.append(rating)
            count +=1

    with open('movieratings/fixtures/stars.json', 'w') as f:
        f.write(json.dumps(ratings))


# need movie
# need rater
# confirm 'rater' vs 'user'