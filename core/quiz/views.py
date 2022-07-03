from rest_framework import generics
from rest_framework.views import APIView
from .serializers import QuizSerializer, RandomQuestionSerializer
from .models import Category, Quiz, Question, Answer
from rest_framework.response import Response

class QuizAPIView(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=False)
        return Response(serializer.data, safe=False)