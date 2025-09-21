from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from account.models import RecruiterProfile
from account.serializers import RecruiterProfileSerializer
from account.permissions import IsRecruiter

class RecruiterProfileView(RetrieveUpdateAPIView):
    serializer_class = RecruiterProfileSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_object(self):
        """Return the logged-in user's recruiter profile."""
        user = self.request.user
        return get_object_or_404(RecruiterProfile, user=user)
