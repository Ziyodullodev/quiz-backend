from rest_framework import serializers
from .models import QuizCategory, Quiz, Answer, QuizTaker, QuizQuestion


class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategory
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'



class QuizQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizQuestion
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['answers'] = AnswerSerializer(instance.get_all_answers(), many=True, read_only=True).data
        return representation


class QuizTakerSerializer(serializers.ModelSerializer):
    percent =  serializers.SerializerMethodField(read_only=True)
    umumiy = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = QuizTaker
        fields = '__all__'

    def get_percent(self, obj):
        quiz_answers = obj.quiz.get_answers_count()
        percent = int((quiz_answers/obj.correct_answers) * 100)
        self.umumiy = quiz_answers
        return str(percent) + " %"

    def get_umumiy(self, obj):
        return self.umumiy

