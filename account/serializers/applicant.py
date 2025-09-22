from rest_framework import serializers
from account.models import (
    Certification,
    Education,
    Experience,
    Project,
    Skill,
    Training,
    Applicant,
)


class EducationSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Education
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Skill
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
        fields = "__all__"
        read_only_fields = ("id", "user", "email")
