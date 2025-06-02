from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Course, Lesson, Enrollment, LessonProgress
from .serializers import (
    CategorySerializer, CourseSerializer, LessonSerializer,
    EnrollmentSerializer, LessonProgressSerializer
)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Course.objects.filter(is_active=True)
        category_id = self.request.query_params.get('category', None)
        difficulty = self.request.query_params.get('difficulty', None)
        
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
            
        return queryset

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, is_active=True)
    
    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course,
        defaults={'status': 'active'}
    )
    
    if created:
        return Response({
            'message': 'Inscrição realizada com sucesso!',
            'enrollment': EnrollmentSerializer(enrollment).data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'message': 'Você já está inscrito neste curso.',
            'enrollment': EnrollmentSerializer(enrollment).data
        })

class MyCoursesView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_lesson_progress(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    enrollment = get_object_or_404(
        Enrollment, 
        student=request.user, 
        course=lesson.course
    )
    
    progress, created = LessonProgress.objects.get_or_create(
        enrollment=enrollment,
        lesson=lesson
    )
    
    progress.completion_percentage = request.data.get('completion_percentage', 0)
    progress.time_spent_minutes = request.data.get('time_spent_minutes', 0)
    progress.is_completed = request.data.get('is_completed', False)
    
    if progress.is_completed and not progress.completed_at:
        from django.utils import timezone
        progress.completed_at = timezone.now()
    
    progress.save()
    
    # Atualizar progresso geral do curso
    total_lessons = enrollment.course.lessons.count()
    completed_lessons = LessonProgress.objects.filter(
        enrollment=enrollment, 
        is_completed=True
    ).count()
    
    enrollment.progress_percentage = (completed_lessons / total_lessons) * 100 if total_lessons > 0 else 0
    if enrollment.progress_percentage >= 100:
        enrollment.status = 'completed'
        enrollment.completed_at = timezone.now()
    
    enrollment.save()
    
    return Response({
        'message': 'Progresso atualizado com sucesso!',
        'progress': LessonProgressSerializer(progress).data,
        'course_progress': enrollment.progress_percentage
    })