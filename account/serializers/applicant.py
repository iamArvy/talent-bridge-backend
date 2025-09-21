from rest_framework import serializers
from account.models import (
    Certification,
    Education,
    Experience,
    Project,
    ApplicantSkill,
    Training,
    ApplicantProfile,
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


class ApplicantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantProfile
        fields = "__all__"
