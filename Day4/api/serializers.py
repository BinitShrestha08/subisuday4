from rest_framework import serializers
from api.models import OLT


class OltSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= OLT
        fields = '__all__'