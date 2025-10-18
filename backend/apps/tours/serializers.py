from rest_framework import serializers
from .models import Tour
from apps.places.models import Place
from apps.places.serializers import PlaceSerializer


class TourSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    place_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Place.objects.all(), write_only=True, source="places"
    )

    class Meta:
        model = Tour
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "image",
            "price",
            "duration",
            "places",
            "place_ids",
            "created_at",
            "updated_at",
        ]
