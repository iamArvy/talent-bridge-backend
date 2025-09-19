from django.contrib import admin
from account.models import RecruiterProfile


@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "headline",
        "industry",
        "years_of_experience",
        "verified",
        "total_hires",
    )
    search_fields = ("user__email", "headline", "industry")
    list_filter = ("verified", "industry")
