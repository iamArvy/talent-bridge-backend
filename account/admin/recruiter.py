from django.contrib import admin
from account.models import Recruiter


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "industry",
        "years_of_experience",
        "verified",
        "total_hires",
    )
    search_fields = ("user__email", "headline", "industry")
    list_filter = ("verified", "industry")
