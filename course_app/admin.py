from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


@admin.register(Category, Course, Lesson, Assignment, Exam, Question, Answer)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'full_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'experience', 'teacher_role')
    list_filter = ('teacher_role',)
    search_fields = ('username', 'full_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'student_role')
    list_filter = ('student_role',)
    search_fields = ('username', 'full_name')


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'links_url')
    search_fields = ('links_url',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'issued_at')
    list_filter = ('course',)


@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'rating')
    list_filter = ('rating', 'course')
    search_fields = ('comment',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_date')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'course', 'quantity')