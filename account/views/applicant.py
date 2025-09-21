from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from account.permissions import IsApplicant
from account.models import (
    ApplicantProfile,
    Certification,
    Education,
    Experience,
    Project,
    ApplicantSkill,
    Training,
)
from account.serializers import (
    ApplicantProfileSerializer,
    CertificationSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    ApplicantSkillSerializer,
    TrainingSerializer,
)


class ApplicantProfileView(RetrieveUpdateAPIView):
    serializer_class = ApplicantProfileSerializer
    permission_classes = [IsAuthenticated, IsApplicant]

    def get_object(self):
        """Return the logged-in user's applicant profile."""
        user = self.request.user
        return get_object_or_404(ApplicantProfile, user=user)


class ApplicantOwnedModelViewSet(ModelViewSet):
    """Base class for models linked to ApplicantProfile."""

    permission_classes = [IsAuthenticated, IsApplicant]

    def get_applicant_profile(self):
        return get_object_or_404(ApplicantProfile, user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(applicant=self.get_applicant_profile())

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return self.queryset.none()
        return self.queryset.filter(applicant=self.get_applicant_profile())


class CertificationViewSet(ApplicantOwnedModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class EducationViewSet(ApplicantOwnedModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(ApplicantOwnedModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ProjectViewSet(ApplicantOwnedModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ApplicantSkillViewSet(ApplicantOwnedModelViewSet):
    queryset = ApplicantSkill.objects.all()
    serializer_class = ApplicantSkillSerializer


class TrainingViewSet(ApplicantOwnedModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
