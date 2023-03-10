from django.shortcuts import render, redirect
from django.db import connection, connections
from MusicDatabase.models import Artist

def index(request):

    # run a sql query
    sqlQuery = "SELECT artist.id, artist.Name, artist.Formed from artist  order by artist.Formed asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        # not always necessary but a good idea
        connection.close()

    return render(request, "MusicDatabase/index.html", {
        "artists":rows
    })
