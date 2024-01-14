from rest_framework.serializers import ModelSerializer
from .models import QuizCategory, Quiz, Answer, QuizTaker


class QuizCategorySerializer(ModelSerializer):
    model = QuizCategory

    class Meta:
        fields = '__all__'

    

class QuizSerializer(ModelSerializer):
    model = Quiz

    class Meta:
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    model = Answer

    class Meta:
        fields = '__all__'


class QuizTakerSerializer(ModelSerializer):
    model = QuizTaker

    class Meta:
        fields = '__all__'