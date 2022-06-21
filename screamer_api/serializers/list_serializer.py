
from rest_framework import serializers
from screamer_api.models import List


class ListSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = List
        fields = ('id', 'title', 'user_id', 'movie_id')
        depth = 1