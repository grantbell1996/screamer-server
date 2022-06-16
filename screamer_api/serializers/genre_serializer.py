from rest_framework import serializers
from screamer_api.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Genre
        fields = ('id', 'title')
        depth = 1