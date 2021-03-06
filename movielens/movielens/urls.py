"""movielens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from citizens import views as citizens_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', citizens_views.login, name='user_login'),
    # url(r'^register/$', citizen_views.user_register, name='user_register'),
    # url(r'^logout/$', citizen_views.user_logout, name='user_logout'),
    # url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^', include('movieapp.urls'))   # looks in app for url code.
    # url(r'^movieapp/', include('movieapp.urls'))  # add 'movieapp/' prefix
    # url(r'^citizen/', include('citizens.urls'))   # add 'citizen/'prefix
]
