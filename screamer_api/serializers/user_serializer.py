from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        depth = 1