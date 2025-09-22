from rest_framework import serializers
from .models import Job, JobApplication


class JobSerializer(serializers.ModelSerializer):
    recruiter = serializers.ReadOnlyField(source="recruiter.id")

    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = ("created_at", "id")


class JobApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.ReadOnlyField(source="applicant.id")

    class Meta:
        model = JobApplication
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "id", "status", "applicant")
    
    def update(self, instance, validated_data):
        """
        Prevent updates except status (which is handled in a special view).
        """
        raise serializers.ValidationError("Applications cannot be updated after creation.")
