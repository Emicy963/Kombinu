from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import QuizDetailSerializer, QuizGenerationSerializer
from .models import Quiz, Content
from .services import generate_quiz_from_opentdb


class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

class QuizGenerationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, content_id):
        # Verifica se o usuário é um criador
        if request.user.user_type != "creator":
            return Response({"error": "Only creators can generate quizzes."}, status=status.HTTP_403_FORBIDDEN)
        content = get_object_or_404(Content, id=content_id)
        serializer = QuizGenerationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        difficulty = serializer.validated_data.get("difficulty")
        number_of_questions = serializer.validated_data.get("number_of_questions")

        # Verifica se já um quiz para este conteúdo
        if hasattr(content, "quiz"):
            return Response({"error": "A quiz already exists for this content."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Chama o serviço para gerar o quiz
        quiz = generate_quiz_from_opentdb(content, difficulty, number_of_questions)

        if quiz:
            return Response({
                "message": "Quiz generated successfuly",
                "quiz_id": str(quiz.pk),
                "content_id": str(content.pk)
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Failed to generate quiz from Open Trivia DB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
