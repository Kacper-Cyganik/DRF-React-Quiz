from rest_framework import serializers
from .models import Category, Quiz, Question, Answer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['title']


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
    quiz = QuizSerializer(many=False, read_only=True)
    class Meta:
        model = Question
        fields = [
            'quiz',
            'title',
            'answers',
        ]

