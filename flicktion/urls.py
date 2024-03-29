"""flicktion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from recommender.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view()),
    url(r'^api/users/$', UsersView.as_view()),
    url(r'^api/users/register/$', UserRegisterView.as_view()),
    url(r'^api/users/update/$', UserUpdateView.as_view()),
    url(r'^api/users/watchlist/$', UserWatchlistView.as_view()),
    url(r'^api/users/wishlist/$', UserWishlistView.as_view()),
    url(r'^api/users/rate/$', RateMovieView.as_view()),
    url(r'^api/users/unrate/$', UnRateMovieView.as_view()),
    url(r'^api/users/wish/$', WishMovieView.as_view()),
    url(r'^api/users/unwish/$', UnWishMovieView.as_view()),
    url(r'^api/users/recommend/$', UserRecommendationsListView.as_view()),
    url(r'^api/movies/$', MoviesDictView.as_view()),
    url(r'^api/moviesList/$', MoviesListView.as_view()),
    url(r'^api/movies/details/$', MovieDetailsView.as_view()),
    url(r'^api/movies/neighbours/$', MovieNeighboursListView.as_view()),
    url(r'^api/movies/neighbours/normalized/$', MovieNormalizedNeighboursListView.as_view()),
    url(r'^api/movies/recommend/$', MovieRecommendationsListView.as_view()),
]
