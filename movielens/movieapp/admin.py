from django.contrib import admin
from .models import Rater, Movie, Rating

# Register your models here.
'''
Will look at variables created within the defined models for display (in html).
The 'list_display' must align with model variables.

The class defines the Django admin.
The admin.site.register links the model to the admin definition.
The list diplay identifies the variables to be passed onto the display.
'''


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'age']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'average_rating']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater', 'movie', 'stars']


admin.site.register(Rater, RaterAdmin)  # links Rater model to the RaterAdmin.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
