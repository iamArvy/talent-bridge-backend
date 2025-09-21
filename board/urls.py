from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")
router.register("applications", JobApplicationViewSet, basename="application")

urlpatterns = [
    path("", include(router.urls)),
]
