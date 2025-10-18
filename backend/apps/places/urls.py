from .views import PlaceViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"places", PlaceViewSet, basename="place")
router.register(r"categories", CategoryViewSet, basename="category")


urlpatterns = router.urls
