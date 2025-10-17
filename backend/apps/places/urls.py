from .views import PlaceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"places", PlaceViewSet, basename="place")

urlpatterns = router.urls
