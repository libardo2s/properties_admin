from rest_framework import serializers
from property_app.models import PropertyType


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ("id", "name")
