from django.contrib import admin
from account.models import (
    Applicant,
    Skill,
    Education,
    Experience,
    Project,
    Certification,
    Training,
)


# Inline Classes (for Applicant)


class SkillInline(admin.TabularInline):
    model = Skill
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
        SkillInline,
        EducationInline,
        ExperienceInline,
        ProjectInline,
        CertificationInline,
        TrainingInline,
    ]
