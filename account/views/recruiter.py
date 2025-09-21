from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from account.models import Recruiter
from account.serializers import RecruiterSerializer
from account.permissions import IsRecruiter


class RecruiterView(RetrieveUpdateAPIView):
    serializer_class = RecruiterSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_object(self):
        """Return the logged-in user's recruiter profile."""
        user = self.request.user
        return get_object_or_404(Recruiter, user=user)
