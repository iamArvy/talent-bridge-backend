from django.contrib import admin
from account.models import Recruiter


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "industry",
        "years_of_experience",
        "total_hires",
    )
    search_fields = ("user__email", "headline", "industry")
