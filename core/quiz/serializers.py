from rest_framework import serializers
from .models import Category, Quiz, Question, Answer

class QuizSerializer(serializers.ModelSerializer):
    
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Quiz
        fields = ['title', 'category']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'title',
            'answers',
        ]

