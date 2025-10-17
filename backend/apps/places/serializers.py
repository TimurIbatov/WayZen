from rest_framework import serializers
from .models import Place
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


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
