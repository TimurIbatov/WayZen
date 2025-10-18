from rest_framework import viewsets, permissions
from .models import Tour
from .serializers import TourSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all().order_by("-created_at")
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]
