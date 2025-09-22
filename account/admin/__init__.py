from .user import UserAdmin, UserChangeForm, UserCreationForm
from .profile import RecruiterAdmin, ApplicantAdmin
from .applicant import (
    SkillAdmin,
    EducationAdmin,
    ExperienceAdmin,
    ProjectAdmin,
    CertificationAdmin,
    TrainingAdmin,
)

__all__ = [
    "UserAdmin",
    "UserChangeForm",
    "UserCreationForm",
    "RecruiterAdmin",
    "ApplicantAdmin",
    "SkillAdmin",
    "EducationAdmin",
    "ExperienceAdmin",
    "ProjectAdmin",
    "CertificationAdmin",
    "TrainingAdmin",
]
