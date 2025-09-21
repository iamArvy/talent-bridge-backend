from rest_framework import serializers
from account.models import Recruiter


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "bio",
            "industry",
            "years_of_experience",
            "agency_name",
            "website",
            "linkedin",
            "location",
            "verified",
            "total_hires",
            "user",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "verified": {"read_only": True},
            "total_hires": {"read_only": True},
            "user": {"read_only": True},
        }


# fields = ["id", "email", "password", "role"]
#
