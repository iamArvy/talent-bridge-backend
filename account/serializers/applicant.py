from rest_framework import serializers
from account.models import (
    Certification,
    Education,
    Experience,
    Project,
    ApplicantSkill,
    Training,
    Applicant,
)
from .skill import SkillSerializer


class EducationSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Education
        fields = "__all__"


class ApplicantSkillSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = ApplicantSkill
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Certification
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Training
        fields = "__all__"


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = [
            "id",
            "first_name",
            "last_name",
            "headline",
            "professional_summary",
            "email",
            "phone",
            "user",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True},
        }
