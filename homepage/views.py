from django.shortcuts import render
from movie.models import Movie


# session é um variavel que está associada à request
def homepage(request):
    """ """
    last_visited = []
    movie_ids = request.session.get("last_visited")
    if movie_ids is not None:
        for movie_id in movie_ids:
            movie = Movie.objects.get(id=movie_id)
            last_visited.append(movie)

    return render(request, 'homepage.html',
                  {'last_visited':last_visited})


