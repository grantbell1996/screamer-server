from rest_framework import serializers
from screamer_api.models import ProductionCompany


class ProductionCompanySerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = ProductionCompany
        fields = ('id', 'name', 'year_founded', 'location')
        depth = 1