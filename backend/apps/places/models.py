from django.db import models
from django.conf import settings
from apps.categories.models import Category
from django.utils.translation import gettext_lazy as _


class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="places"
    )
    address = models.CharField(max_length=500, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    image = models.ImageField(
        _("Изображение"), upload_to="zones/", blank=True, null=True
    )
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    price_range = models.CharField(
        max_length=8, blank=True, help_text="Напр., '$', '$$'"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    def __str__(self):
        return f"{self.user} → {self.place}"
