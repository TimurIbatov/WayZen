from rest_framework import viewsets, permissions, status
from .models import Tour, FavoriteTour
from .serializers import TourSerializer, FavoriteTourSerializer
from rest_framework.response import Response


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all().order_by("-created_at")
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = FavoriteTour.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.AllowAny]


class FavoriteTourViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteTourSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteTour.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # предотвращаем дублирование
        instance, created = FavoriteTour.objects.get_or_create(
            user=self.request.user, tour=serializer.validated_data["tour"]
        )
        if not created:
            raise serializers.ValidationError("Этот тур уже в избранном.")
        return instance

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
