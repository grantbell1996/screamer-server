"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screamer_api.serializers import ActorSerializer
from screamer_api.models import Actor

class ActorView(ViewSet):
    """actors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single actor type
        
        Returns:
            Response -- JSON serialized actor type
        """
        actor = Actor.objects.get(pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all actors"""


        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized actor instance
        """
        actor = Actor.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            birth_date=request.data["birth_date"],
            death_date=request.data["death_date"],
            bio=request.data["bio"],
            image=request.data["image"]
        )

        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a actor

        Returns:
            Response -- Empty body with 204 status code
        """

        actor = Actor.objects.get(pk=pk)
        actor.first_name=request.data["first_name"]
        actor.last_name=request.data["last_name"]
        actor.birth_date=request.data["birth_date"]
        actor.death_date=request.data["death_date"]
        actor.bio=request.data["bio"]
        actor.image=request.data["image"]
        
        
        actor.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        actor = Actor.objects.get(pk=pk)
        actor.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

