from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import QuizDetailSerializer
from .models import Quiz


class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
