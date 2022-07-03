
from django.urls import path
from . import views

app_name='quiz'

urlpatterns = [
    path('quiz/', views.QuizAPIView.as_view(), name='quiz-list')
]
