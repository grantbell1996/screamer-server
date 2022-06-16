"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screamer_api.models.Director import Director
from screamer_api.models.Movie import Movie
from screamer_api.models.Genre import Genre
from screamer_api.serializers import ActorSerializer, MovieSerializer
from screamer_api.models import Actor

class MovieView(ViewSet):
    """actors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single actor type
        
        Returns:
            Response -- JSON serialized actor type
        """
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all actors"""


        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized actor instance
        """
        director = Director.objects.get(pk=request.data["director"])
        genre = Genre.objects.get(pk=request.data["genre"])
        
        movie = Movie.objects.create(
            name = request.data["name"],
            release_date = request.data["release_date"],
            run_time = request.data["run_time"],
            filming_location = request.data["filming_location"],
            synopsis = request.data["synopsis"],
            trailer = request.data["trailer"],
            poster = request.data["poster"],
            user = request.auth.user,
            genre = genre,
            director = director
            )

        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a movie

        Returns:
            Response -- Empty body with 204 status code
        """

        movie = Movie.objects.get(pk=pk)
        movie.name = request.data["name"]
        movie.release_date = request.data["release_date"]
        movie.run_time = request.data["run_time"]
        movie.filming_location = request.data["filming_location"]
        movie.synopsis = request.data["synopsis"]
        movie.user = request.auth.user
        movie.trailer = request.data["trailer"]
        movie.poster = request.data["poster"]
        
        director = Director.objects.get(pk=request.data["director"])
        movie.director = director
        
        genre = Genre.objects.get(pk=request.data["genre"])
        movie.genre = genre
        
        movie.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

