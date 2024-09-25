from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', views.results, name='results'),
    path('reset/', views.reset_answers, name='reset_answers'),
]