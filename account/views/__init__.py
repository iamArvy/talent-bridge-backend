from .auth import RegisterView, LoginView, RefreshTokenView
from .applicant import ApplicantProfileView, CertificationViewSet, EducationViewSet, ExperienceViewSet, ProjectViewSet, ApplicantSkillViewSet, TrainingViewSet
from .recruiter import RecruiterProfileView
from .skill import SkillViewSet
# from .user import User, MyUserManager
# from .recruiter import RecruiterProfile
# from .applicant import (
#     ApplicantProfile,
#     ApplicantSkill,
#     Project,
#     Education,
#     Training,
#     Certification,
#     Experience,
# )
# from .skill import Skill


__all__ = [
    "RegisterView",
    "LoginView",
    "RefreshTokenView",
    "ApplicantProfileView",
    "RecruiterProfileView",
    "CertificationViewSet",
    "EducationViewSet",
    "ExperienceViewSet",
    "ProjectViewSet",
    "ApplicantSkillViewSet",
    "TrainingViewSet",
    "SkillViewSet"
    # "ProfileViewSet"
    # "User",
    # "MyUserManager",
    # "RecruiterProfile",
    # "Skill",
    # "ApplicantProfile",
    # "ApplicantSkill",
    # "Project",
    # "Education",
    # "Training",
    # "Certification",
    # "Experience",
]
