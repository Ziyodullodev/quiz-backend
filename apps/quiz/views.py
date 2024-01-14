from .serializers import QuizCategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from utils.rest_framework.list_api_view import MyListAPIView, MyListCreateAPIView
from .models import QuizCategory, Quiz, Question, Answer
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