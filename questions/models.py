from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('oop', 'ООП'),
        ('data_structures', 'Структуры и типы данных'),
        ('git', 'Git'),
        ('linux', 'Linux'),
        ('docker', 'Docker'),
        ('sql', 'SQL'),
        ('network_protocols', 'Сетевые протоколы'),
        ('django', 'Django'),
    ]

    text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='python')

    def __str__(self):
        return self.text


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class UserAnswer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1500)
    is_correct = models.BooleanField()