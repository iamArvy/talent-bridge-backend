from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
from .permissions import IsRecruiterOrReadOnly, IsApplicantOrReadOnly, IsRecruiterOfJob


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiterOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user.recruiter)


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsApplicantOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user.applicant)

    def update(self, request, *args, **kwargs):
        return Response({"error": "Applications cannot be updated"}, status=405)

    def partial_update(self, request, *args, **kwargs):
        return Response({"error": "Applications cannot be updated"}, status=405)

    @action(
        detail=True,
        methods=["patch"],
        permission_classes=[permissions.IsAuthenticated, IsRecruiterOfJob],
    )
    def change_status(self, request, pk=None):
        """Recruiter changes application status"""
        application = self.get_object()
        new_status = request.data.get("status")

        if new_status not in dict(JobApplication.APPLICATION_STATUS_CHOICES):
            return Response(
                {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
            )

        application.status = new_status
        application.save()
        return Response({"status": "updated", "new_status": application.status})
