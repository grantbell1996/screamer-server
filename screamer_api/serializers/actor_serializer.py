from rest_framework import serializers
from screamer_api.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Actor
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'death_date', 'bio', 'image')
        depth = 1