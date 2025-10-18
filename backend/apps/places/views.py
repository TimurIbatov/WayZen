from .models import Place
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import api_view, permission_classes
from .models import Place, Category, Favorite
from .serializers import PlaceSerializer, CategorySerializer, FavoriteSerializer
from django.contrib.auth import authenticate
from django.db.models import Q


# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.select_related("category").all().order_by("-created_at")
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        q = request.query_params.get("q") or request.query_params.get("search")
        category = request.query_params.get("category")
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")
        radius_km = request.query_params.get("radius")  # радиус в км

        # Поиск по имени, описанию, адресу или категории
        if q:
            qs = qs.filter(
                Q(name__icontains=q)
                | Q(description__icontains=q)
                | Q(address__icontains=q)
                | Q(category__name__icontains=q)
            )

        # Фильтр по категории (slug или id)
        if category:
            qs = qs.filter(Q(category__slug=category) | Q(category__id=category))

        # Простейшая гео-фильтрация (bounding box)
        try:
            if lat and lon and radius_km:
                lat = float(lat)
                lon = float(lon)
                r = float(radius_km)
                delta = r / 111.0  # приближённо: 1° ≈ 111 км
                qs = qs.filter(
                    latitude__gte=lat - delta,
                    latitude__lte=lat + delta,
                    longitude__gte=lon - delta,
                    longitude__lte=lon + delta,
                )
        except Exception:
            pass

        return qs


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
