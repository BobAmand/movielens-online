from django.db import models

# Create your models here.
'''
Three models are contained to control
   Rater = the individual rating the movie.
   Movie = the movie title.
   Rating = links the rater and movie by star rating.
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
        return (str(self.id))

class Movie(models.Model):

    class Meta:
        verbose_name_plural = 'movies'

    title = models.CharField(max_length=255, null=True)
        # minimized the list of data available; genria is in View Git

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']
        # 'stars__avg' is dynamically calculating the average.
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

        
