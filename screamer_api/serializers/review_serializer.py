from rest_framework import serializers
from screamer_api.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'body', 'rating')
        depth = 1