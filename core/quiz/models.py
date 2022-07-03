from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(
        Category, null=True, blank=True, default=1, on_delete=models.SET_NULL)
    title = models.CharField(
        max_length=255, default='New Quiz', verbose_name='Quiz Title')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['id']

    def __str__(self) -> str:
        return self.title


class Updated(models.Model):

    date_updated = models.DateTimeField(
        verbose_name='Last Updated', auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    )

    TYPE = (
        (0, 'Multiple Choice'),
    )

    quiz = models.ForeignKey(
        Quiz, null=True, related_name='questions', on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, verbose_name="Title")
    question_type = models.IntegerField(
        choices=TYPE, default=0, verbose_name="Type of Question")
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name="Difficulty")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Date Created")
    is_active = models.BooleanField(
        default=False, verbose_name='Active Status')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']


class Answer(Updated):

    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['id']
    
