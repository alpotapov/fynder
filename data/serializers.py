from data.models import Venue, VenueToTag, Tag
from rest_framework import serializers


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue