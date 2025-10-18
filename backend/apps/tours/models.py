from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Tour(models.Model):
    name = models.CharField(_("Название тура"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(_("Описание"), blank=True)
    image = models.ImageField(
        _("Изображение тура"), upload_to="tours/", null=True, blank=True
    )
    places = models.ManyToManyField(
        "places.Place", related_name="tours", verbose_name=_("Места")
    )
    price = models.DecimalField(
        _("Цена"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    duration = models.DurationField(_("Продолжительность"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Тур")
        verbose_name_plural = _("Туры")

    def __str__(self):
        return self.name


class FavoriteTour(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite_tours",
    )
    slug = models.SlugField(max_length=200, unique=True)
    icon = models.CharField(
        max_length=8, blank=True, help_text="Emoji или короткий значок"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
