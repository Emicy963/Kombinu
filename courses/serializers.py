from rest_framework import serializers
from .models import Category, Course, Lesson, Enrollment, LessonProgress

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.get_full_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    total_lessons = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_total_lessons(self, obj):
        return obj.lessons.count()

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = '__all__'

class LessonProgressSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    
    class Meta:
        model = LessonProgress
        fields = '__all__'
