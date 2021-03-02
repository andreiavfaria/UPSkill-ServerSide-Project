from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
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
    last_visited = request.session.get("last_visited", [])
    if movie.id in last_visited:
        last_visited = list(filter(lambda x: x != movie.id, last_visited))

    last_visited.insert(0, movie.id)
    last_visited = last_visited[:5]
    request.session["last_visited"] = last_visited
    # a lista actualizada vai para o session
    request.session.modified = True

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


@login_required
def movie_review(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST) # prepopular formulario com os dados do comentario
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.movie = movie
            new_review.user = request.user
            try:
                new_review.save()
            except IntegrityError:
                return redirect('movie:movie_edit_review', movie_id=movie_id)
                # do url movie, vamos querer o edit_review

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


@login_required
def edit_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = movie.reviews.get(user=request.user)
    # raise RuntimeError(review)
    if request.method == 'POST':
        review_form = ReviewForm(instance=review,
                                 data=request.POST)
        # verifica a validade
        if review_form.is_valid():
            review_form.save()
            return redirect(movie) # depois do edit redireciona para o filme

    else:
        review_form = ReviewForm(instance=review)

    return render(request,
                  'movie/review.html',
                  {
                      'movie': movie,
                      'review_form': review_form,
                      'edit':True,
                   }) # variaveis de contexto