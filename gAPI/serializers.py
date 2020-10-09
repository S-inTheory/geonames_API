from rest_framework.serializers import ModelSerializer

from gAPI.models import Geoname


class GeonameSerializer(ModelSerializer):
    class Meta:
        model = Geoname
        fields = '__all__'
