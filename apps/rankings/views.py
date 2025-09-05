from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from quizzes.models import QuizSubmission
from accounts.models import CustomUser


class GlobalRankingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Calcula o score total por usuário
        user_scores = (
            QuizSubmission.objects.values("user_id")
            .annotate(total_score=Sum("score"))
            .order_by("-total_score")
        )

        # Formata os top users
        top_users_data = []
        for i, score_data in enumerate(user_scores[:100]):  # Apenas os top 100
            try:
                user = CustomUser.objects.get(pk=score_data["user_id"])
                top_users_data.append(
                    {
                        "user_id": score_data["user_id"],
                        "email": user.email,
                        "total_score": score_data["total_score"],
                        "position": i + 1,
                    }
                )
            except CustomUser.DoesNotExist:
                continue  # Ignore usuários que foram deletados

        # Encontra a posição do usuário logado
        current_user_id = request.user.pk
        current_user_score_entry = next(
            (item for item in user_scores if item["user_id"] == current_user_id), None
        )
        currente_user_total_score = (
            current_user_score_entry["total_score"] if current_user_score_entry else 0
        )

        # Calcular a posição
        current_user_position = 1
        for score_data in user_scores:
            if score_data["total_score"] > currente_user_total_score:
                current_user_position += 1
            elif score_data["user_id"] == current_user_id:
                break  # Usuário foi encontrado, posição é a atual

        user_position_data = {
            "position": current_user_position,
            "total_score": currente_user_total_score,
        }

        return Response(
            {"top_users": top_users_data, "user_position": user_position_data},
            status=status.HTTP_200_OK,
        )
