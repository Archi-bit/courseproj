from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *



class UserListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return UserProfileSerializer(*args, **kwargs)

    def get(self, request):
        objects = UserProfile.objects.all()
        serializer = UserProfileSerializer(objects, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class UserDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return UserProfileSerializer(*args, **kwargs)

    def get(self, request, pk):
        userprofile = get_object_or_404(
            UserProfile,
            pk=pk
        )
        serializer = UserProfileSerializer(userprofile)

        return Response(serializer.data)

    def put(self, request, pk):
        objects = get_object_or_404(
            UserProfile,
            pk=pk
        )
        serializer = UserProfileSerializer(
            objects,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):
        object = get_object_or_404(
            UserProfile,
            pk=pk
        )
        serializer = UserProfileSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        object = get_object_or_404(
            UserProfile,
            pk=pk
        )
        object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TeaherListView(APIView):

    def get_serializer(self, *args, **kwargs):
            return TeacherSerializer(*args, **kwargs)

    def get(self, request):
        objects = Teacher.objects.all()
        serializer = TeacherSerializer(objects, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TeacherDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return TeacherSerializer(*args, **kwargs)

    def get(self, request, pk):
        teacher = get_object_or_404(
            Teacher,
            pk=pk
        )
        serializer = TeacherSerializer(teacher)

        return Response(serializer.data)

    def put(self, request, pk):
        objects = get_object_or_404(
            Teacher,
            pk=pk
        )
        serializer = TeacherSerializer(
            objects,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):
        objects = get_object_or_404(
            Teacher,
            pk=pk,
        )
        serializer = TeacherSerializer(
            objects,
            data=request.data,
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        objects = get_object_or_404(
            Teacher,
            pk=pk
        )

        objects.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return StudentSerializer(*args, **kwargs)

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class StudentDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return StudentSerializer(*args, **kwargs)

    def get(self, request, pk):
        objects = get_object_or_404(
            Student,
            pk=pk
        )
        serializer = StudentSerializer(objects)

        return Response(serializer.data)

    def put(self, request, pk):
        objects = get_object_or_404(
            Student,
            pk=pk
        )
        serializer = StudentSerializer(
            objects,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):
        objects = get_object_or_404(
            Student,
            pk=pk
        )
        serializer = StudentSerializer(
            objects,
            data=serializer.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        objects = get_object_or_404(
            Student,
            pk=pk
        )
        objects.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LinkListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return LinkSerializer(*args, **kwargs)

    def get(self, request):
        objects = Links.objects.all()
        serializer = LinkSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = LinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LinkDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return LinkSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Links, pk=pk)
        serializer = LinkSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Links, pk=pk)
        serializer = LinkSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        object = get_object_or_404(Links, pk=pk)
        serializer = LinkSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        object = get_object_or_404(Links, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CategorySerializer(*args, **kwargs)

    def get(self, request):
        objects = Category.objects.all()
        serializer = CategorySerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CategoryDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CategorySerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Category, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CourseListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CourseSerializer(*args, **kwargs)

    def get(self, request):
        objects = Course.objects.all()
        serializer = CourseSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CourseDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CourseSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Course, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return LessonSerializer(*args, **kwargs)

    def get(self, request):
        objects = Lesson.objects.all()
        serializer = LessonSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = LessonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LessonDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return LessonSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Lesson, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignmentListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return AssignmentSerializer(*args, **kwargs)

    def get(self, request):
        objects = Assignment.objects.all()
        serializer = AssignmentSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AssignmentDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return AssignmentSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Assignment, pk=pk)
        serializer = AssignmentSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Assignment, pk=pk)
        serializer = AssignmentSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Assignment, pk=pk)
        serializer = AssignmentSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Assignment, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExamListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return ExamSerializer(*args, **kwargs)

    def get(self, request):
        objects = Exam.objects.all()
        serializer = ExamSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ExamDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return ExamSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Exam, pk=pk)
        serializer = ExamSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Exam, pk=pk)
        serializer = ExamSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Exam, pk=pk)
        serializer = ExamSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Exam, pk=pk)
        object.delete()
       
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return QuestionSerializer(*args, **kwargs)

    def get(self, request):
        objects = Question.objects.all()
        serializer = QuestionSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class QuestionDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return QuestionSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Question, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return AnswerSerializer(*args, **kwargs)

    def get(self, request):
        objects = Answer.objects.all()
        serializer = AnswerSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AnswerDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return AnswerSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Answer, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class CertificateListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CertificateSerializer(*args, **kwargs)

    def get(self, request):
        objects = Certificate.objects.all()
        serializer = CertificateSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CertificateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CertificateDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CertificateSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Certificate, pk=pk)
        serializer = CertificateSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Certificate, pk=pk)
        serializer = CertificateSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Certificate, pk=pk)
        serializer = CertificateSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Certificate, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseReviewListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CourseSerializer(*args, **kwargs)

    def get(self, request):
        objects = CourseReview.objects.all()
        serializer = CourseReviewSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CourseReviewDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CourseSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(CourseReview, pk=pk)
        serializer = CourseReviewSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(CourseReview, pk=pk)
        serializer = CourseReviewSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(CourseReview, pk=pk)
        serializer = CourseReviewSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(CourseReview, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CourseSerializer(*args, **kwargs)

    def get(self, request):
        objects = Cart.objects.all()
        serializer = CartSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CartDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CartSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(Cart, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartItemListView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CartItemSerializer(*args, **kwargs)

    def get(self, request):
        objects = CartItem.objects.all()
        serializer = CartItemSerializer(objects, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CartItemDetailView(APIView):

    def get_serializer(self, *args, **kwargs):
        return CartItemSerializer(*args, **kwargs)

    def get(self, request, pk):
        object = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(object)
        
        return Response(serializer.data)

    def put(self, request, pk):
        object = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        object = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = get_object_or_404(CartItem, pk=pk)
        object.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)