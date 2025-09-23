from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
from .permissions import IsRecruiterOrReadOnly, IsRecruiterOfJob
from account.permissions import IsApplicant, IsRecruiter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from .swagger_params import job_filter_params
from .filters import JobFilter, JobApplicationFilter

# Create your views here.


class ApplicationViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Only supports retrieving a single application
    + custom change_status action
    """

    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_applicant():
            return JobApplication.objects.filter(applicant=user)
        elif user.is_recruiter():
            return JobApplication.objects.filter(job__recruiter=user)
        return JobApplication.objects.none()

    @action(
        detail=True,
        methods=["patch"],
        url_path="change_status",
        permission_classes=[permissions.IsAuthenticated, IsRecruiterOfJob],
    )
    def change_status(self, request, pk=None):
        application = self.get_object()
        new_status = request.data.get("status")
        if new_status not in dict(JobApplication.APPLICATION_STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=400)
        application.status = new_status
        application.save()
        return Response({"status": "updated", "new_status": application.status})


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiterOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = JobFilter
    search_fields = ["title", "description", "company", "requirements"]
    ordering_fields = ["created_at", "salary_min", "salary_max"]

    def perform_create(self, serializer):
        serializer.save(
            recruiter=self.request.user,
            recruiter_profile=self.request.user.recruiter_profile,
        )

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[permissions.IsAuthenticated, IsApplicant],
        url_path="apply",
    )
    def apply(self, request, pk=None):
        job = self.get_object()
        if JobApplication.objects.filter(job=job, applicant=request.user).exists():
            return Response(
                {"error": "You have already applied to this job."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = JobApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(job=job, applicant=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[permissions.IsAuthenticated, IsRecruiterOfJob],
        url_path="applications",
    )
    def applications(self, request, pk=None):
        job = self.get_object()
        applications = job.applications.all()
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=job_filter_params)
    def list(self, request, *args, **kwargs):
        """List all jobs with filters, search and ordering"""
        return super().list(request, *args, **kwargs)


class ApplicantApplicationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Applicant can only list their own applications
    at /applicant/applications/
    """

    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["status", "job"]
    search_fields = ["cover_letter", "job__title", "job__company"]
    ordering_fields = ["created_at", "updated_at", "status"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user)


class JobApplicationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Recruiter can only list applications for their own jobs
    at /jobs/{job_id}/applications/
    """

    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiterOfJob]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = JobApplicationFilter
    search_fields = ["job__title", "applicant__email"]
    ordering_fields = ["created_at", "status"]

    def get_queryset(self):
        job_id = self.kwargs.get("id")
        return JobApplication.objects.filter(job_id=job_id)


class RecruiterJobViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Recruiter can only list their own jobs
    at /recruiter/jobs/
    """

    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        return Job.objects.filter(recruiter=self.request.user)
