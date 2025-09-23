import django_filters
from .models import Job, JobApplication


class JobFilter(django_filters.FilterSet):
    salary_min = django_filters.NumberFilter(field_name="salary_min", lookup_expr="gte")
    salary_max = django_filters.NumberFilter(field_name="salary_max", lookup_expr="lte")
    location = django_filters.CharFilter(lookup_expr="icontains")
    type = django_filters.CharFilter(lookup_expr="iexact")
    industry = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Job
        fields = ["location", "type", "industry", "salary_min", "salary_max"]


class JobApplicationFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    created_after = django_filters.DateFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_before = django_filters.DateFilter(
        field_name="created_at", lookup_expr="lte"
    )

    class Meta:
        model = JobApplication
        fields = ["status", "created_at"]
