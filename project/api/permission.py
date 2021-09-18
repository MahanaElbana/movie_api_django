from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

   #def has_permission(self, request, view):
   #    is_admin = bool(request.user and request.user.is_authenticated)
   #    return request.method == 'GET' or is_admin
   #                        or
   def has_permission(self, request, view):
       
      if request.method in permissions.SAFE_METHODS:
            return True

      else :
          return bool(request.user and request.user.is_authenticated)


class ReviewReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        else :
          return obj.user_review == request.user
