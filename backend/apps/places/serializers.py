from dataclasses import field
from rest_framework import serializers
from .models import Favorite, Place, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "icon"]


class PlaceSerializer(serializers.ModelSerializer):
    # При чтении — вложенный сериализатор категории.
    # При создании/обновлении можно передавать category_id.
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        required=False,
    )

    class Meta:
        model = Place
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "category",
            "category_id",
            "address",
            "latitude",
            "longitude",
            "images",
            "rating",
            "price_range",
            "is_hidden_gem",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_images(self, value):
        # Простая валидация: images должен быть списком строк (URL-ов)
        if value is None:
            return []
        if not isinstance(value, list):
            raise serializers.ValidationError("images must be a list of URLs")
        # Можно добавить проверку каждого URL-а
        return value


class FavoriteSerializer(serializers.ModelSerializer):
    place_id = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(), source="place", write_only=True
    )
    place = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Favorite
        fields = ["id", "place", "place_id"]

    def validate(self, attrs):
        user = self.context["request"].user
        place = attrs["place"]

        if Favorite.objects.filter(user=user, place=place).exists():
            raise serializers.ValidationError("Место уже добавлено в избранное.")
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        return Favorite.objects.create(user=user, **validated_data)
