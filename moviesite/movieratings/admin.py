from django.contrib import admin
from .models import Rater, Movies, Ratings

# Register your models here.
class RaterDisplay(admin.ModelAdmin):
    pass
class MoviesDisplay(admin.ModelAdmin):
    pass
class RatingsDisplay(admin.ModelAdmin):
    pass
#    list_display = ['age', 'occupation']

admin.site.register(Rater, RaterDisplay)
admin.site.register(Movies, MoviesDisplay)
admin.site.register(Ratings, RatingsDisplay)
