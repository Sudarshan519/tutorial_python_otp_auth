from rest_framework import permissions
from snippets import serializers

from snippets.groups import is_employer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return False

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

# class EmployerOrReadOnly(permissions.BasePermission):


def is_employee(user):
    return user.groups.filter(name='Employee').exists()


from django.contrib.auth.decorators import user_passes_test

def my_view(request):
    pass

class IsEmployer(permissions.BasePermission):
    # @user_passes_test(is_employer)
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return False
     
        # Write permissions are only allowed to the owner of the snippet.
        # return obj.owner == request.user
        return False#//request.user.groups.filter(name='Employer').exists()