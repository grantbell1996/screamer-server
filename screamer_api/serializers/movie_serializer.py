from rest_framework import serializers
from screamer_api.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Movie
        fields = ('id', 'movie_id', 'name', 'director', 'release_date', 'run_time', 'filming_location', 'synopsis', 'user', 'trailer', 'genre', 'poster', 'actor')
        depth = 1