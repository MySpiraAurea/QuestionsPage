# Generated by Django 4.2.16 on 2024-09-24 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('python', 'Python'), ('oop', 'ООП'), ('data_structures', 'Структуры и типы данных'), ('git', 'Git'), ('linux', 'Linux'), ('docker', 'Docker'), ('sql', 'SQL'), ('network_protocols', 'Сетевые протоколы'), ('django', 'Django')], default='python', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1500)),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.test')),
            ],
        ),
    ]
