from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
# need to return an http response
def index(request):
    return HttpResponse("Welcome to the MovieLens Dataset.")
#     return HttpResponse("this is the response")

def top_twenty(movie):
     #top-20 rated movies
    return HttpResponse(blab.objects.order_by('-average_rating')[:20])

'''
simple views:
   start with poinitng url
'''
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)    #movie detail
    # ratings = movie.ratings_set.all()
    # user_ratings =[]
    # for rating in ratings:
    #     user_ratings.append([rating.id])
    return render(request,
                'movieratings/movie_detail.html',
                {'movie': movie})       #pass the movie object/simple

# def rater_detail(request, rater_id):
#     movie = Movie.objects.get(pk=movie_id)    #movie detail
#     for rating in rater.rating_set.all():
#         movie_ratings.append({
#             'movie': rating.movie,
#             'stars': '&rating.starts,
#         })
#     return render(request,
#                 'movieratings/movie_detail.html',
#                 {'movie': movie})       #pass the movie object/simple
