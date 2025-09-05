from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Content
from .serializers import ContentListSerializer, ContentSerializer
from .permissions import IsCreator


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["title", "description"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentListSerializer
        return ContentSerializer

    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer
        """
        if self.action == "create":
            permission_classes = [IsCreator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        has_quiz_param = self.request.query_params.get("has_quiz", None)
        if has_quiz_param is not None:
            if has_quiz_param.lower() == "true":
                queryset = queryset.filter(quiz__isnull=False)
            elif has_quiz_param.lower() == "false":
                queryset = queryset.filter(quiz__isnull=True)
        return queryset
