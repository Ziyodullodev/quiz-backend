from .serializers import QuizCategorySerializer, QuizSerializer, AnswerSerializer, QuizTakerSerializer
from utils.rest_framework.list_api_view import MyListAPIView, MyListCreateAPIView
from .models import QuizCategory, Quiz, Answer, QuizTaker
from utils.rest_framework.pagination import MyPagination
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from rest_framework import status

# Create your views here.


class QuizCategoryListAPIView(MyListCreateAPIView):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuizCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuizListAPIView(MyListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class QuizDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class AnswerListAPIView(MyListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


class AnswerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']


class QuizTakerListAPIView(MyListCreateAPIView):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', 'quiz']

    
class QuizTakerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', 'quiz']
