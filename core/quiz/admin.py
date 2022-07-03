from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
    list_display = [
        'name'
    ]

@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    model = models.Quiz
    list_display = [
        'id',
        'title'
    ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right',
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    model = models.Question
    fields = [
        'title',
        'quiz',
    ]
    
    list_display = [
        'title',
        'quiz',
        'date_updated',
    ]

    inlines = [AnswerInlineModel,]

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    model = models.Answer
    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]