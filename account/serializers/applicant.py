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


class CertificationSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Certification
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Education
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ApplicantSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = ApplicantSkill
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Training
        fields = "__all__"


class ApplicantProfileSerializer(serializers.ModelSerializer):
    certifications = CertificationSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    skills = ApplicantSkillSerializer(many=True, read_only=True)
    trainings = TrainingSerializer(many=True, read_only=True)

    def get_experiences(self, obj):
        experiences = obj.experiences.order_by("-start_date")[:3]
        return ExperienceSerializer(experiences, many=True).data

    def get_certifications(self, obj):
        experiences = obj.certifications.order_by("-start_date")[:3]
        return CertificationSerializer(experiences, many=True).data

    class Meta:
        model = ApplicantProfile
        fields = "__all__"
