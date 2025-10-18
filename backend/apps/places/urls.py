from .views import PlaceViewSet, CategoryViewSet, FavoriteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"places", PlaceViewSet, basename="place")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"favorites", FavoriteViewSet, basename="favorite")


urlpatterns = router.urls
