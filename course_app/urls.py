from django.contrib import admin
from django.urls import path

from .views import *



urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('teachers/', TeaherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('students/', StudentListView.as_view(), name='student-name'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='stusent-detail'),
    path('links/', LinkListView.as_view(), name='links-list'),
    path('links/<int:pk>/', LinkDetailView.as_view(), name='links-detail'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('courses/', CourseListView.as_view(), name='courses-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='courses-detail'),
    path('lessons/', LessonListView.as_view(), name='lesson=list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('assignment/', AssignmentListView.as_view(), name='assignment-list'),
    path('assignment/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('questions/', QuestionListView.as_view(), name='questoins-list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('answers/', AnswerListView.as_view(), name='answers-list'),
    path('answers/<int:pk>/', AnswerDetailView.as_view(), name='asnwer-detail'),
    path('certificates/', CertificateListView.as_view(), name='certificates-list'),
    path('certificates/<int:pk>/', CertificateDetailView.as_view(), name='certificate-detail'),
    path('reviews/', CourseListView.as_view(), name='course-review-list'),
    path('reviews/<int:pk>/', CourseDetailView.as_view(), name='course-review-detail'),
    path('carts/', CartListView.as_view(), name='carts-list'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cart_item/', CartItemListView.as_view(), name='cart-items-list'),
    path('cart_item/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail')
]