from rest_framework.routers import DefaultRouter

from livekit.viewsets.livekit import LivekitViewset

router = DefaultRouter()

router.register("", LivekitViewset, basename="livekit")

urlpatterns = router.urls
