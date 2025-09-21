from .auth import RegisterSerializer, LoginSerializer
from .recruiter import RecruiterProfileSerializer
from .applicant import (ApplicantProfileSerializer, CertificationSerializer, EducationSerializer, ExperienceSerializer, ProjectSerializer, ApplicantSkillSerializer, TrainingSerializer)
from .skill import SkillSerializer
__all__ = [
    "RegisterSerializer",
    "LoginSerializer",
    "RecruiterProfileSerializer",
    "ApplicantProfileSerializer",
    "CertificationSerializer",
    "EducationSerializer",
    "ExperienceSerializer",
    "ProjectSerializer",
    "ApplicantSkillSerializer",
    "TrainingSerializer",
    "SkillSerializer"
]
