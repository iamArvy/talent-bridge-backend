from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
from .permissions import IsRecruiterOrReadOnly, IsApplicantOrReadOnly, IsRecruiterOfJob
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class JobFilter(django_filters.FilterSet):
    salary_min = django_filters.NumberFilter(field_name="salary_min", lookup_expr="gte")
    salary_max = django_filters.NumberFilter(field_name="salary_max", lookup_expr="lte")
    location = django_filters.CharFilter(lookup_expr="icontains")
    type = django_filters.CharFilter(lookup_expr="iexact")
    industry = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Job
        fields = ["location", "type", "industry", "salary_min", "salary_max"]


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
        serializer.save(recruiter=self.request.user)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "location",
                openapi.IN_QUERY,
                description="Filter by location",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "type",
                openapi.IN_QUERY,
                description="Filter by job type",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "industry",
                openapi.IN_QUERY,
                description="Filter by industry",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "salary_min",
                openapi.IN_QUERY,
                description="Filter by min salary",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "salary_max",
                openapi.IN_QUERY,
                description="Filter by max salary",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search jobs",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "ordering",
                openapi.IN_QUERY,
                description="Order by fields",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        """List all jobs with filters, search and ordering"""
        return super().list(request, *args, **kwargs)


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsApplicantOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = JobFilter
    search_fields = ["title", "description", "company", "requirements"]
    ordering_fields = ["created_at", "salary_min", "salary_max"]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

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
