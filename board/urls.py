from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from .views import (
    JobViewSet,
    RecruiterJobViewSet,
    ApplicantApplicationViewSet,
    JobApplicationViewSet,
    ApplicationViewSet,
)

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")
(router.register("recruiter/jobs", RecruiterJobViewSet, basename="recruiter-job"),)
router.register(
    "applicant/applications",
    ApplicantApplicationViewSet,
    basename="applicant-application",
)
router.register("applications", ApplicationViewSet, basename="application")
jobs_router = NestedDefaultRouter(router, r"jobs", lookup="job")
jobs_router.register(
    r"applications", JobApplicationViewSet, basename="job-applications"
)

urlpatterns = [
    path("", include(router.urls)),
]
