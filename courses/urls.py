from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('', views.CourseListView.as_view(), name='courses'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('<int:course_id>/enroll/', views.enroll_course, name='enroll-course'),
    path('my-courses/', views.MyCoursesView.as_view(), name='my-courses'),
    path('lessons/<int:lesson_id>/progress/', views.update_lesson_progress, name='lesson-progress'),
]
