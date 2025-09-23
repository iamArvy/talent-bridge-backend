from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from account.permissions import IsApplicant
from account.models import (
    Certification,
    Education,
    Experience,
    Project,
    Skill,
    Training,
)
from account.serializers import (
    CertificationSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    SkillSerializer,
    TrainingSerializer,
)


class ApplicantOwnedModelViewSet(ModelViewSet):
    """Base class for models linked to Applicant."""

    permission_classes = [IsAuthenticated, IsApplicant]

    def get_applicant(self):
        return self.request.user.applicant_profile

    def perform_create(self, serializer):
        serializer.save(applicant=self.get_applicant())

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return self.queryset.none()
        return self.queryset.filter(user=self.request.user)


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


class SkillViewSet(ApplicantOwnedModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class TrainingViewSet(ApplicantOwnedModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
