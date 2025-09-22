from django.contrib import admin
from .models import Job, JobApplication


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location_type",
        "type",
        "salary_min",
        "salary_max",
        "recruiter",
        "end_date",
        "created_at",
    )
    search_fields = ("title", "company", "location", "industry")
    list_filter = ("type", "location_type", "salary_min", "salary_max", "recruiter")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "applicant", "status", "created_at")
    search_fields = ("job__title", "applicant__user__email")
    list_filter = ("status", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")