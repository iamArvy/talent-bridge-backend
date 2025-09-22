# account/urls.py
from django.urls import path, include
from .views import (
    RegisterView,
    LoginView,
    RefreshTokenView,
    ApplicantView,
    RecruiterView,
    CertificationViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ProjectViewSet,
    SkillViewSet,
    TrainingViewSet,
)
from rest_framework.routers import DefaultRouter

# Auth URLs
authUrlPatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]

# Applicant Routers
applicant_router = DefaultRouter()
applicant_router.register(
    "certifications", CertificationViewSet, basename="applicant-certification"
)
applicant_router.register("education", EducationViewSet, basename="applicant-education")
applicant_router.register(
    "experiences", ExperienceViewSet, basename="applicant-experience"
)
applicant_router.register("projects", ProjectViewSet, basename="applicant-project")
applicant_router.register("skills", SkillViewSet, basename="applicant-skill")
applicant_router.register("trainings", TrainingViewSet, basename="applicant-training")

# Main Urls
urlpatterns = [
    path("auth/", include(authUrlPatterns)),
    path("applicant/", ApplicantView.as_view(), name="applicant-profile"),
    path("recruiter/", RecruiterView.as_view(), name="recruiter-profile"),
    path("", include(applicant_router.urls)),
]
