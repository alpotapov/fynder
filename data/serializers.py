from data.models import Venue, Category
from rest_framework import serializers


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue