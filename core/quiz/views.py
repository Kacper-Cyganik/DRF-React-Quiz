from rest_framework import generics
from rest_framework.views import APIView
from .serializers import QuizSerializer, QuestionSerializer
from .models import Category, Quiz, Question, Answer
from rest_framework.response import Response

class QuizAPIView(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestionAPIView(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestionsAPIView(APIView):

    def get(self, request, format=None, **kwargs):
        questions = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)