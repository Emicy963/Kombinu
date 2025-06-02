from rest_framework import serializers
from .models import Category, Course, Lesson, Enrollment, LessonProgress

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    class Meta:
        model = Category
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    """Serializer for Lesson model."""
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course model."""
    instructor_name = serializers.CharField(source='instructor.get_full_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    total_lessons = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_total_lessons(self, obj):
        """Calculate the total number of lessons in the course.
        Args:
            obj (Course): The course instance.
        Returns:
            int: The total number of lessons in the course.
        """
        return obj.lessons.count()

class EnrollmentSerializer(serializers.ModelSerializer):
    """Serializer for Enrollment model."""
    course = CourseSerializer(read_only=True)
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = '__all__'

class LessonProgressSerializer(serializers.ModelSerializer):
    """Serializer for LessonProgress model."""
    lesson = LessonSerializer(read_only=True)
    
    class Meta:
        model = LessonProgress
        fields = '__all__'
