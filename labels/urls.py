from rest_framework.routers import DefaultRouter
from labels.views import PlacemarksPhoto, PolygonView

router = DefaultRouter()
router.register('placemarks', viewset=PlacemarksPhoto)
router.register('polygons', viewset=PolygonView)

urlpatterns = router.urls
