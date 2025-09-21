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
    ApplicantSkillViewSet,
    TrainingViewSet,
    SkillViewSet,
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
applicant_router.register(
    "certifications", CertificationViewSet, basename="applicant-certification"
)
applicant_router.register("education", EducationViewSet, basename="applicant-education")
applicant_router.register(
    "experiences", ExperienceViewSet, basename="applicant-experience"
)
applicant_router.register("projects", ProjectViewSet, basename="applicant-project")
applicant_router.register("skills", ApplicantSkillViewSet, basename="applicant-skill")
applicant_router.register("trainings", TrainingViewSet, basename="applicant-training")

applicantUrlpatterns = [
    path("profile/", include(applicant_router.urls)),
    path("", ApplicantView.as_view(), name="applicant-profile"),
]

# Recruiter Routers
recruiterUrlpatterns = [
    path("", RecruiterView.as_view(), name="recruiter-profile"),
]

# Main Urls
urlpatterns = [
    path("auth/", include(authUrlPatterns)),
    path("applicant/", include(applicantUrlpatterns)),
    path("recruiter/", include(recruiterUrlpatterns)),
    path("", include(router.urls)),
]

# {
#   "first_name": "Oluwaseyi",
#   "last_name": "Oke",
#   "headline": "Web Developer",
#   "professional_summary": "I am a Web Developer",
#   "email": "user@example.com",
#   "phone": "08109229601",
#   "user": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
# }
