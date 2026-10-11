from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('teacher', 'Teacher'),
    )

    full_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Teacher(UserProfile):
    experience = models.PositiveSmallIntegerField()
    TEACHER_ROLE_CHOICES = (
        ('teacher', 'Teacher'),
    )

    teacher_role = models.CharField(max_length=20, choices=TEACHER_ROLE_CHOICES)
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Student(UserProfile):
    STUDENT_ROLE_CHOICES = (
        ('client', 'Client'),
    )

    student_role = models.CharField(max_length=20, choices=STUDENT_ROLE_CHOICES)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Links(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    links_url = models.URLField()

    def __str__(self):
        return f'{self.student.username} - link'


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category.category_name} - {self.course_name} - {self.level} - {self.price} - {self.created_by}'


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=255)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_lesson


class Assignment(models.Model):
    name_assignment = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.name_assignment} - {self.course.course_name}'


class Exam(models.Model):
    name_exam = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.name_exam} - экзамен по {self.course.course_name}'


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name_question = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f'{self.exam.name_exam} - ответ {self.name_question}'


class Answer(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.TextField()
    true_answers = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.questions.name_question} - {self.true_answers}'


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return f'{self.student.username} - по курсу {self.course.course_name}'


class CourseReview(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.course.course_name} - {self.rating}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - cart'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.course.course_name} - {self.quantity}'

    def get_total_price(self):
        return self.course.price * self.quantity