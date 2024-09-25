# questions/management/commands/import_questions.py
from django.core.management.base import BaseCommand
from questions.models import Question
import json


class Command(BaseCommand):
    help = 'Import questions from a JSON file'

    def handle(self, *args, **kwargs):
        with open('questions.json', 'r') as f:
            data = json.load(f)
        for item in data:
            Question.objects.create(
                text=item['text'],
                category=item['category'],
                correct_answer=item['correct_answer'],
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported questions'))
