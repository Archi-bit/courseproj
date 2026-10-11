from rest_framework import serializers

from .models import *



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'profile_picture', 'full_name', 'role')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'username', 'experience', 'teacher_role')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture', 'student_role')


class LinkSerializer(serializers.ModelSerializer):

    student = StudentSerializer(read_only=True)

    class Meta:
        model = Links
        fields = ('id', 'student')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'category', 'course_name', 'description', 'level', 'price', 'created_by', 'created_at')


class LessonSerializer(serializers.ModelSerializer):

    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'name_lesson', 'video_url', 'course')


class AssignmentSerializer(serializers.ModelSerializer):

    course = CourseSerializer(read_only=True)

    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = ('id', 'name_assignment', 'due_date', 'course', 'students')


class ExamSerializer(serializers.ModelSerializer):

    course = CourseSerializer(read_only=True)

    class Meta:
        model = Exam
        fields = ('id', 'name_exam', 'course', 'passing_score', 'duration')


class QuestionSerializer(serializers.ModelSerializer):

    exam = ExamSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'exam', 'name_question', 'text')


class AnswerSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'questions', 'answers', 'true_answers')


class CertificateSerializer(serializers.ModelSerializer):

    course = CourseSerializer(read_only=True)

    student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Certificate
        fields = ('id', 'student', 'course', 'issued_at', 'certificate_url')


class CourseReviewSerializer(serializers.ModelSerializer):

    course = CourseSerializer(read_only=True)
    
    user = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'user', 'course', 'rating', 'comment')


class CartSerializer(serializers.ModelSerializer):

    user = StudentSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_date')


class CartItemSerializer(serializers.ModelSerializer):

    cart = CartSerializer(read_only=True)

    course = CourseSerializer(read_only=True)

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'course', 'quantity', 'total_price')

    def get_total_price(self, obj):
        return obj.get_total_price()