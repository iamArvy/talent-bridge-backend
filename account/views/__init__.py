from .auth import RegisterView, LoginView, RefreshTokenView
from .applicant import (
    ApplicantView,
    CertificationViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ProjectViewSet,
    ApplicantSkillViewSet,
    TrainingViewSet,
)
from .recruiter import RecruiterView
from .skill import SkillViewSet
# from .user import User, MyUserManager
# from .recruiter import Recruiter
# from .applicant import (
#     Applicant,
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
    "ApplicantView",
    "RecruiterView",
    "CertificationViewSet",
    "EducationViewSet",
    "ExperienceViewSet",
    "ProjectViewSet",
    "ApplicantSkillViewSet",
    "TrainingViewSet",
    "SkillViewSet",
    # "ProfileViewSet"
    # "User",
    # "MyUserManager",
    # "Recruiter",
    # "Skill",
    # "Applicant",
    # "ApplicantSkill",
    # "Project",
    # "Education",
    # "Training",
    # "Certification",
    # "Experience",
]
