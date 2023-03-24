from django.shortcuts import render, redirect
from django.db import connection, connections
# from MusicDatabase.models import Artist

def index(request):

    # run a sql query
    sqlQuery = "SELECT Artist.ID, Artist.Name, Artist.Formed from Artist ORDER BY Artist.Formed asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        # not always necessary but a good idea
        connection.close()

    return render(request, "MusicDatabase/index.html", {
        "artists":rows
    })


def indexWithSort(request, sort):
    if sort == "name" or sort == "id" or sort == "formed":
        sqlQuery = "SELECT Artist.ID, Artist.Name, Artist.Formed FROM Artist ORDER BY Artist." + sort
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            rows = list(cursor.fetchall())
            cursor.close()
            connection.close()

        return render(request, "MusicDatabase/index.html", {
            "artists":rows
        })

def ArtistsAlbums(request, aID):
    sqlQuery = "SELECT Artist.Name, Artist.ID, Album.ID, Album.AlbumName, Album.YearReleased FROM Artist "
    sqlQuery += "INNER JOIN Album ON Artist.ID = Album.ArtistID "
    sqlQuery+= "WHERE Artist.ID = " + str(aID) + " ORDER BY album.YearReleased"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close() 

    return render(request, "MusicDatabase/albums.html", {
        "albums":rows
    })

