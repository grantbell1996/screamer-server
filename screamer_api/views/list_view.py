"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screamer_api.models.Director import Director
from screamer_api.models.List import List
from screamer_api.models.Genre import Genre
from screamer_api.models.Movie import Movie
from screamer_api.serializers import ActorSerializer, ListSerializer
from screamer_api.models import Actor

class ListView(ViewSet):
    """actors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single actor type
        
        Returns:
            Response -- JSON serialized actor type
        """
        list = List.objects.get(pk=pk)
        serializer = ListSerializer(list)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all actors"""


        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized actor instance
        """
        movie_id = Movie.objects.get(pk=request.data["movie"])
        
        list = List.objects.create(
            title = request.data["title"],
            user = request.auth.user,
            movie_id = movie_id
            )
        
        serializer = ListSerializer(list)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a list

        Returns:
            Response -- Empty body with 204 status code
        """

        list = List.objects.get(pk=pk)
        list.title = request.data["title"]
        list.user = request.auth.user
        
        movie_id = Movie.objects.get(pk=request.data["movie"])
        list.movie_id = movie_id
        
        list.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        list = List.objects.get(pk=pk)
        list.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

