from .user import UserAdmin, UserChangeForm, UserCreationForm
from .recruiter import RecruiterAdmin
from .applicant import (
    ApplicantAdmin,
)
from .skill import SkillAdmin


__all__ = [
    "UserAdmin",
    "UserChangeForm",
    "UserCreationForm",
    "RecruiterAdmin",
    "ApplicantAdmin",
    "SkillAdmin",
]
