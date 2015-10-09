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
