# account/urls.py
from django.urls import path, include
from .views import (
    RegisterView, LoginView, RefreshTokenView,
    ApplicantProfileView, RecruiterProfileView,
    CertificationViewSet, EducationViewSet, ExperienceViewSet,
    ProjectViewSet, ApplicantSkillViewSet, TrainingViewSet, SkillViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"skills", SkillViewSet, basename="skill")

# Auth URLs
authUrlPatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]

# Applicant Routers
applicant_router = DefaultRouter()
applicant_router.register("certifications", CertificationViewSet, basename="applicant-certification")
applicant_router.register("education", EducationViewSet, basename="applicant-education")
applicant_router.register("experiences", ExperienceViewSet, basename="applicant-experience")
applicant_router.register("projects", ProjectViewSet, basename="applicant-project")
applicant_router.register("skills", ApplicantSkillViewSet, basename="applicant-skill")
applicant_router.register("trainings", TrainingViewSet, basename="applicant-training")

applicantUrlpatterns = [
    path("profile/", include(applicant_router.urls)),
    path("profile/", ApplicantProfileView.as_view(), name="applicant-profile"),
]

# Recruiter Routers
recruiterUrlpatterns = [
    path("profile", RecruiterProfileView.as_view(), name="recruiter-profile"),
]

# Main Urls
urlpatterns = [
    path("auth/", include(authUrlPatterns)),
    path("applicant/", include(applicantUrlpatterns)),
    path("recruiter/", include(recruiterUrlpatterns)),
    path("", include(router.urls)),
]
