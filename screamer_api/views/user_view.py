"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from screamer_api.serializers.user_serializer import UserSerializer

class UserView(ViewSet):
    """actors view"""

    def list(self, request):
        """Handle GET requests for single actor type
        
        Returns:
            Response -- JSON serialized actor type
        """
        serializer = UserSerializer(request.auth.user)
        return Response(serializer.data)
