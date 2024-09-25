from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.questions, name='questions'),
]