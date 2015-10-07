from django.contrib import admin
from .models import Rater, Movie, Rating

# Register your models here.
class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'occupation']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'average_rating']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'item_id', 'rating']

admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
