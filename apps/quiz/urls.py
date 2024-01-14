from django.urls import path
from .views import *

urlpatterns = [
    path('quiz-category/', QuizCategoryListAPIView.as_view(), name="quiz-category-list"),
    path('quiz-category/<int:pk>/', QuizCategoryDetailAPIView.as_view(), name="quiz-category-detail"),

    path('quiz/', QuizListAPIView.as_view(), name="quiz-list"),
    path('quiz/<int:pk>/', QuizDetailAPIView.as_view(), name="quiz-detail"),

    path('answer/', AnswerListAPIView.as_view(), name="answer-list"),
    path('answer/<int:pk>/', AnswerDetailAPIView.as_view(), name="answer-detail"),

    path('quiz-taker/', QuizTakerListAPIView.as_view(), name="quiz-taker-list"),
    path('quiz-taker/<int:pk>/', QuizTakerDetailAPIView.as_view(), name="quiz-taker-detail"),
]
