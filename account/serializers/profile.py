from rest_framework import serializers
from account.models import Applicant, Recruiter


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = "__all__"
        read_only_fields = ("id", "verified", "total_hires", "user")


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
        read_only_fields = ("id", "user")
