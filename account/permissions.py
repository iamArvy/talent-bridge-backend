from rest_framework.permissions import BasePermission


class IsApplicant(BasePermission):
    """Allow access only to applicants."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "applicant")


class IsRecruiter(BasePermission):
    """Allow access only to recruiters."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "recruiter")
