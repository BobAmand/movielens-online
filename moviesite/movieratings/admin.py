from django.contrib import admin
from .models import Rater, Movie, Rating

# Register your models here.
class RaterDisplay(admin.ModelAdmin):
    list_display = ['age', 'occupation']

class MovieDisplay(admin.ModelAdmin):
    list_display = ['movie_id', 'title']

class RatingDisplay(admin.ModelAdmin):
    list_display = ['user_id', 'item_id', 'rating']

admin.site.register(Rater, RaterDisplay)
admin.site.register(Movie, MovieDisplay)
admin.site.register(Rating, RatingDisplay)
