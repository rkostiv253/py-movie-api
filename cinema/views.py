from django.http import JsonResponse
from rest_framework.generics import get_object_or_404

from cinema.models import Movie
from cinema.serializers import MovieSerializer


def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


def movie_detail(request, pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=200)


def movie_create(request):
    if request.method == "POST":
        movie = Movie.objects.create()
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=201)


def movie_update(request, pk):
    if request.method == "PUT":
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=200)


def movie_delete(request, pk):
    if request.method == "DELETE":
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return JsonResponse({}, status=204)
