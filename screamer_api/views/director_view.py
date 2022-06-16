"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from screamer_api.serializers import DirectorSerializer
from screamer_api.models import Director, Movie

class DirectorView(ViewSet):
    """directors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single director type
        
        Returns:
            Response -- JSON serialized director type
        """
        director = Director.objects.get(pk=pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all directors"""


        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized director instance
        """
        
        director = Director.objects.create(
            first_name = request.data["first_name"],
            last_name = request.data["last_name"],
            birth_date = request.data["birth_date"],
            death_date = request.data["death_date"],
            bio = request.data["bio"],
            image=request.data["image"]
        )

        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a director

        Returns:
            Response -- Empty body with 204 status code
        """

        director = Director.objects.get(pk=pk)
        director.first_name=request.data["first_name"]
        director.last_name=request.data["last_name"]
        director.birth_date=request.data["birth_date"]
        director.death_date=request.data["death_date"]
        director.bio=request.data["bio"]
        director.image=request.data["image"]
        
        director.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        director = Director.objects.get(pk=pk)
        director.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
