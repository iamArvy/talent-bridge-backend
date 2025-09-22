from django.contrib import admin
from account.models import Applicant, Recruiter


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("user", "headline", "email", "phone")
    search_fields = ("user__email", "headline", "email")


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "industry",
        "years_of_experience",
        "total_hires",
    )
    search_fields = ("user__email", "headline", "industry")
