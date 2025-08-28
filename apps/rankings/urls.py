from django.urls import path
from .views import GlobalRankingView


urlpatterns = [
    path("global/", GlobalRankingView.as_view(), name="ranking-global"),
]

