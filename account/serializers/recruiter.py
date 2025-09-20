from rest_framework import serializers
from account.models import RecruiterProfile

class RecruiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterProfile
        fields = "__all__"
