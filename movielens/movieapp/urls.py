from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'movie/(?P<movie_id>\d+)$', views.movie_detail),   # a movie page
    url(r'rater/(?P<rater_id>\d+)$', views.rater_detail),   # a rater page

]
