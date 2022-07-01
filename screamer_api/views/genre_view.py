"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screamer_api.models.Director import Director
from screamer_api.models.Movie import Movie
from screamer_api.models.Genre import Genre
from screamer_api.serializers import GenreSerializer
from screamer_api.models import Actor

class GenreView(ViewSet):
    """actors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single actor type
        
        Returns:
            Response -- JSON serialized actor type
        """
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all actors"""


        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    

