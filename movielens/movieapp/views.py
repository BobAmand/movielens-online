from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Movie, Rater


# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)    # lookup from Movie dict
    return render(request, 'movieapp/movie_detail.html',
                  {'movie': movie})          # passing the movie object in.

def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)    # lookup from Movie dict
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({                 # list of dicts w movies + stars
            'movie': rating.movie,
            'stars': '\u2605' * rating.stars,
        })
    return render(request, 'movieapp/rater_detail.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})  # Added movieratings


def top_movies(request):
    # movie_list = []    -too many hits on database (every Database)
    # for movie in Movie.objects.all():
    #     if type(movie.average_rating()) == float:
    #         movie_list.append(movie)
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)
    # more dunder magic.
    # Advanced Database optimization from class:
    movies = popular_movies.annotate(Avg('rating__stars')) \
                           .order_by('-rating__stars__avg')[:20]

    #  annotate, rating__stars, and -rating__stars__avg [directly from notes]
    #  return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']
    # 'stars__avg' is dynamically calculating the average.

    return render(request,
                  'movieapp/top_movies.html', {'movies': movies})
