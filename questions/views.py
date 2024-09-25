from django.shortcuts import render
from .models import Question, Test, UserAnswer

def questions(request):
    template = 'questions/questions.html'
    
    # Получаем выбранные категории из GET-запроса или сессии
    if request.method == 'GET' and 'categories' in request.GET:
        categories = request.GET.getlist('categories')
        request.session['categories'] = categories
    else:
        categories = request.session.get('categories', [])

    # Получаем все вопросы, на которые пользователь уже ответил
    answered_questions = UserAnswer.objects.filter(test__user=request.user).values_list('question_id', flat=True)

    # Фильтруем вопросы, исключая уже отвеченные
    if categories:
        questions = Question.objects.filter(category__in=categories).exclude(id__in=answered_questions).order_by('id')
    else:
        questions = Question.objects.exclude(id__in=answered_questions).order_by('id')

    show_answer = request.session.get('show_answer', None)

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        question = Question.objects.get(id=question_id)

        if 'show_answer' in request.POST:
            # Показать или скрыть правильный ответ
            if show_answer == str(question_id):
                show_answer = None
            else:
                show_answer = str(question_id)
            request.session['show_answer'] = show_answer
        else:
            answer_status = request.POST.get('answer_status')

            # Удаляем предыдущие ответы на этот вопрос для текущего пользователя
            UserAnswer.objects.filter(test__user=request.user, question=question).delete()

            # Сохраняем новый ответ
            UserAnswer.objects.create(
                test=Test.objects.create(user=request.user),
                question=question,
                answer=answer_status,
                is_correct=(answer_status == 'correct')
            )

            # Обновляем список отвеченных вопросов
            answered_questions = UserAnswer.objects.filter(test__user=request.user).values_list('question_id', flat=True)

            # Получаем новый список вопросов, исключая уже отвеченные
            if categories:
                questions = Question.objects.filter(category__in=categories).exclude(id__in=answered_questions).order_by('id')
            else:
                questions = Question.objects.exclude(id__in=answered_questions).order_by('id')

    return render(request, template, {
        'questions': questions,
        'categories': categories,
        'show_answer': show_answer,
    })

