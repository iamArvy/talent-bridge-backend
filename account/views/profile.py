from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from account.models import Recruiter, Applicant
from account.serializers import RecruiterSerializer, ApplicantSerializer
from account.permissions import IsApplicant, IsRecruiter


class ApplicantProfileView(RetrieveUpdateAPIView):
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated, IsApplicant]

    def get_object(self):
        """Return the logged-in user's profile (applicant)."""
        user = self.request.user
        return get_object_or_404(Applicant, user=user)


class RecruiterProfileView(RetrieveUpdateAPIView):
    serializer_class = RecruiterSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_object(self):
        """Return the logged-in user's profile (recruiter)."""
        user = self.request.user
        return get_object_or_404(Recruiter, user=user)
