
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import ReviewForm


def movie_list(request):
    """ """
    movies = Movie.objects.all()

    return render(request,
                  'movie/list.html',
                  {'movies': movies})


def movie_detail(request, id):
    """ """
    movie = get_object_or_404(Movie, id=id)# verificação de existencia

    return render(request,
                  'movie/detail.html',
                  {'movie': movie}
                  )


def movie_search(request):
    search_string = request.GET.get("query")
    if search_string:
        results = Movie.objects.filter(title__contains=search_string)
    else:
        results = None

    return render(request,
                 'movie/search.html',
                 {'results': results})


def movie_review(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST) # prepopular formulario com os dados do comentario
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.movie = movie
            new_review.user_id = request.user.id
            new_review.save()
            return redirect(movie)
    elif request.method == 'GET':
        review_form = ReviewForm() # isto gera o formulario
        # esta variavel é a que dá nome no {{ form }}

    return render(request,
                  'movie/review.html',
                  {
                      'movie': movie,
                      'review_form': review_form,
                      'new_review': new_review,
                   }) # variaveis de contexto
