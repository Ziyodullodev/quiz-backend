from rest_framework.serializers import ModelSerializer
from .models import QuizCategory, Quiz, Answer, QuizTaker


class QuizCategorySerializer(ModelSerializer):
    class Meta:
        model = QuizCategory
        fields = '__all__'


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuizTakerSerializer(ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = '__all__'
