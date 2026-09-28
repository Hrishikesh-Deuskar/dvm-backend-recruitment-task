from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "top-artists/<str:country>/",
        views.top_artists,
        name="top_artists",
    ),

    path(
        "top-tracks/<str:country>/",
        views.top_tracks,
        name="top_tracks",
    ),

    path(
        "search/artist/",
        views.search_artist,
        name="search_artist",
    ),

    path(
        "search/album/",
        views.search_album,
        name="search_album",
    ),

    path(
        "search/track/",
        views.search_track,
        name="search_track",
    ),

    path(
        "artist-top-tracks/",
        views.artist_top_tracks,
        name="artist_top_tracks",
    ),
]