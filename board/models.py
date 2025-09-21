from django.db import models
import uuid
from account.models import (
    RecruiterProfile,
    ApplicantProfile,
    Experience,
    Education,
    ApplicantSkill,
    Training,
    Certification,
)
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ("internship", "Internship"),
        ("contract", "Contract"),
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
    )

    LOCATION_TYPE_CHOICES = (
        ("in-person", "In-Person"),
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = ArrayField(models.CharField(max_length=255))
    location_type = models.CharField(max_length=12, choices=LOCATION_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=12, choices=JOB_TYPE_CHOICES)
    industry = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_description = models.TextField(blank=True)
    company_website = models.URLField(blank=True)
    salary_min = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    salary_max = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    recruiter = models.ForeignKey(
        RecruiterProfile, on_delete=models.CASCADE, related_name="jobs"
    )
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "title",
                    "industry",
                    "location_type",
                    "type",
                    "salary_min",
                    "salary_max",
                ]
            ),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.title} - {self.company}"


class JobApplication(models.Model):
    APPLICATION_STATUS_CHOICES = (
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(
        ApplicantProfile, on_delete=models.CASCADE, related_name="applications"
    )
    cover_letter = models.TextField()
    education = models.ManyToManyField(Education)
    skills = models.ManyToManyField(ApplicantSkill)
    training = models.ManyToManyField(Training)
    certifications = models.ManyToManyField(Certification)
    experiences = models.ManyToManyField(Experience)
    status = models.CharField(max_length=255, choices=APPLICATION_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["job", "status"]),
            models.Index(fields=["job", "created_at"]),
            models.Index(fields=["applicant", "status"]),
            models.Index(fields=["applicant", "created_at"]),
        ]

    def __str__(self):
        return f"{self.applicant.user.email} - {self.job.title}"
