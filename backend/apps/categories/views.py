from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Category
from .serializers import CategorySerializer
from django.contrib.auth import authenticate


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"
