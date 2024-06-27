from rest_framework import serializers
from property_app.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ("id", "name", "address", "country", "city", "zip_code", "type", "area")
