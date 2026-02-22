from rest_framework.routers import DefaultRouter

from . import views

app_name = "drf_api"
router = DefaultRouter()
router.register("users", views.UserViewSet, "drf-users")

urlpatterns = router.urls
