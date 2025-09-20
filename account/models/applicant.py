from django.db import models
import uuid
from .user import User
from .skill import Skill
from .profiles import ApplicantProfile
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="certifications"
    )
    name = models.CharField(max_length=255) 
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=255, blank=True)
    credential_url = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField("Skill", blank=True, related_name="certifications")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.applicant.id}"


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="education"
    )
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True)
    highlights = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        default=list,
        help_text="List of key learnings or achievements",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.applicant.id} {self.degree} at {self.institution}"


class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="experiences"
    )
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        default=list,
        help_text="List of bullet points describing responsibilities",
    )
    skills = models.ManyToManyField("Skill", blank=True, related_name="experiences")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.applicant.id} {self.title} at {self.company}"


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="projects"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField("Skill", blank=True, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.applicant.id} - {self.name}"


class ApplicantSkill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="skills"
    )
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(
        max_length=20,
        choices=(
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("expert", "Expert"),
        ),
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.applicant.id} - {self.skill.name}"


class Training(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="trainings"
    )
    title = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField("Skill", blank=True, related_name="trainings")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.applicant.id}"
