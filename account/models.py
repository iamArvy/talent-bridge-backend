from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


# Create your models here.
class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ("recruiter", "Recruiter"),
        ("applicant", "Applicant"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def is_applicant(self):
        return self.role == "applicant"

    def is_recruiter(self):
        return self.role == "recruiter"

    def __str__(self):
        return self.email


class RecruiterProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="recruiter_profile"
    )
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    industry = models.CharField(max_length=255, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)

    agency_name = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    verified = models.BooleanField(default=False)
    total_hires = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Recruiter"


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ApplicantProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="applicant_profile"
    )
    headline = models.CharField(max_length=100)
    professional_summary = models.TextField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Applicant"


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


class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="certifications"
    )
    name = models.CharField(max_length=255)  # e.g. "AWS Solutions Architect"
    issuer = models.CharField(max_length=255)  # e.g. "Amazon"
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=255, blank=True)
    credential_url = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField("Skill", blank=True, related_name="certifications")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.applicant.id}"


class Training(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="trainings"
    )
    title = models.CharField(max_length=255)  # e.g. "Agile Project Management"
    provider = models.CharField(max_length=255)  # e.g. "Udemy, Coursera, Local Academy"
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField("Skill", blank=True, related_name="trainings")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.applicant.id}"
