from tabnanny import verbose
from rest_framework.routers import DefaultRouter

from apps.places.models import Favorite
from .views import FavoriteTourViewSet, TourViewSet

router = DefaultRouter()
router.register(r"tours", TourViewSet, basename="tours")
router.register(r"favorites", FavoriteTourViewSet, basename="favorite_tours")

urlpatterns = router.urls
