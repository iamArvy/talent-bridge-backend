from django.contrib import admin
from account.models import (
    Applicant,
    ApplicantSkill,
    Education,
    Experience,
    Project,
    Certification,
    Training,
)


# Inline Classes (for Applicant)


class ApplicantSkillInline(admin.TabularInline):
    model = ApplicantSkill
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1


class TrainingInline(admin.TabularInline):
    model = Training
    extra = 1


# Applicant Admin


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("user", "headline", "email", "phone")
    search_fields = ("user__email", "headline", "email")
    inlines = [
        ApplicantSkillInline,
        EducationInline,
        ExperienceInline,
        ProjectInline,
        CertificationInline,
        TrainingInline,
    ]
