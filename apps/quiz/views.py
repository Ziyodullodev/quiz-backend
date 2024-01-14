from .serializers import QuizCategorySerializer, QuizSerializer, AnswerSerializer, QuizTakerSerializer
from .models import QuizCategory, Quiz, Answer, QuizTaker
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class QuizDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class AnswerListAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


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

    
class QuizTakerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', 'quiz']
