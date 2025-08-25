from rest_framework.permissions import IsAuthenticated


class IsCreator(IsAuthenticated):
    """
    Permissão customizada para permitir apenas usuários do tipo 'creator'.
    """
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.user_type == "creator"
