from django.contrib import admin
from account.models import (
    Skill,
    Education,
    Experience,
    Project,
    Certification,
    Training,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree", "start_date", "end_date")
    search_fields = ("institution", "degree")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "start_date", "end_date")
    search_fields = ("title", "company")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
    search_fields = ("name",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issue_date", "expiration_date")
    search_fields = ("name", "issuer")


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("title", "provider", "start_date", "end_date")
    search_fields = ("title", "provider")
