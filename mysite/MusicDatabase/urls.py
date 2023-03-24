from django.urls import path
from . import views

# tell our server what functions to run when user this specified url

urlpatterns = [
    path("", views.index),
    path("<int:aID>", views.ArtistsAlbums),
    path("<str:sort>", views.indexWithSort),
    # path("albums.html?<str:sort>", views.AlbumInfo)
]
