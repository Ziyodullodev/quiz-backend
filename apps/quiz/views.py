from .serializers import QuizCategorySerializer, QuizSerializer, AnswerSerializer, QuizTakerSerializer, QuizQuestionSerializer
from .models import QuizCategory, Quiz, Answer, QuizTaker, QuizQuestion
from utils.rest_framework.pagination import MyPagination
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from rest_framework import status

# Create your views here.


class QuizCategoryListAPIView(generics.ListCreateAPIView):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class QuizCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class QuizListAPIView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class QuizDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class QuizQuestionListAPIView(generics.ListCreateAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']


class QuizQuestiondetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']



class AnswerListAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    search_fields = ['text', 'quiz']


class AnswerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


class QuizTakerListAPIView(generics.ListCreateAPIView):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', 'quiz']
    pagination_class = MyPagination

    def get_queryset(self):
        user = self.request.user
        # Bu joyda agar user admin bo'lsa hamma javoblar yuboriladi
        if not user.is_staff:
            self.queryset = QuizTaker.objects.filter(user=user)
        return super().get_queryset()


class QuizTakerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', 'quiz']


class ReytingAPIView(generics.ListAPIView):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        answer = QuizTaker.objects.filter(user=self.request.user)
        quiz_answers = answer.quiz.get_answers_count()
        # percent = int((quiz_answers/self.correct_answers) * 100)
        # self.umumiy = quiz_answers
        # return str(percent) + " %"
        # print(answer)
        return super().get_queryset()