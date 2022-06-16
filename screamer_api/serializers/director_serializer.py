from rest_framework import serializers
from screamer_api.models import Director


class DirectorSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Director
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'death_date', 'bio', 'image')
        depth = 1