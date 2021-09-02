from rest_framework.routers import DefaultRouter
from labels.views import PlacemarksPhoto

router = DefaultRouter()
router.register('placemarks', viewset=PlacemarksPhoto)

urlpatterns = router.urls
