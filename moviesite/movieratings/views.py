from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# need to return an http response
def index(request):
    return HttpResponse("Welcome to the MovieLens Dataset.")
#     return HttpResponse("this is the response")

def top_twenty(movie):
     #top-20 rated movies
    return HttpResponse(blab.objects.order_by('-average_rating')[:20])
