from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    icon = models.CharField(
        max_length=8, blank=True, help_text="Emoji или короткий значок"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
