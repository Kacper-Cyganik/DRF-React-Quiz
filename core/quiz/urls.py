
from django.urls import path
from . import views

app_name='quiz'

urlpatterns = [
    path('quiz/', views.QuizAPIView.as_view(), name='quiz-list'),
    path('quiz/rand/<str:topic>/', views.RandomQuestionAPIView.as_view(), name='random-question'),
    path('quiz/<str:topic>/', views.QuizQuestionsAPIView.as_view(), name='quiz-questions'),
    
]
