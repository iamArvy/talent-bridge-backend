from .user import UserAdmin, UserChangeForm, UserCreationForm
from .recruiter import RecruiterProfileAdmin
from .applicant import (
    ApplicantProfileAdmin,
)
from .skill import SkillAdmin


__all__ = [
    "UserAdmin",
    "UserChangeForm",
    "UserCreationForm",
    "RecruiterProfileAdmin",
    "ApplicantProfileAdmin",
    "SkillAdmin",
]
