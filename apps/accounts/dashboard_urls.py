from django.urls import path
from .views import LearnerStatsView, LearnerCoursesView, CreatorStatsView

urlpatterns = [
    path('learner/stats/', LearnerStatsView.as_view(), name='learner-stats'),
    path('learner/courses/', LearnerCoursesView.as_view(), name='learner-courses'),
    path('creator/stats/', CreatorStatsView.as_view(), name='creator-stats'),
]
