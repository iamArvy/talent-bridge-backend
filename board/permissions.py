from rest_framework import permissions


class IsRecruiterOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and getattr(request.user, "role", None) == "recruiter"
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.recruiter.user == request.user


class IsRecruiterOfJob(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.job.recruiter.user == request.user


class IsApplicationOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.job.recruiter.user == request.user
