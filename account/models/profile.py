from django.db import models
import uuid
from .user import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Applicant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="applicant_profile"
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    headline = models.CharField(max_length=100)
    professional_summary = models.TextField(blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Applicant"


class Recruiter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="recruiter_profile"
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True)
    industry = models.CharField(max_length=255, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)

    agency_name = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    total_hires = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Recruiter"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create Applicant or Recruiter
    whenever a new user is created.
    """
    if created:
        if instance.role == "applicant":
            Applicant.objects.create(user=instance)
        elif instance.role == "recruiter":
            Recruiter.objects.create(user=instance)
