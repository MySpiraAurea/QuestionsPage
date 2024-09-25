from django.shortcuts import render, redirect
from questions.models import UserAnswer


def results(request):
    template = 'results/results.html'
    user_answers = UserAnswer.objects.filter(test__user=request.user)

    correct_answers = user_answers.filter(is_correct=True).count()
    incorrect_answers = user_answers.filter(is_correct=False, answer='incorrect').count()
    uncertain_answers = user_answers.filter(is_correct=False, answer='uncertain').count()
    total_answers = user_answers.count()

    correct_percentage = f"{correct_answers} из {total_answers}"
    incorrect_percentage = f"{incorrect_answers} из {total_answers}"
    uncertain_percentage = f"{uncertain_answers} из {total_answers}"

    incorrect_questions = user_answers.filter(answer='incorrect')
    uncertain_questions = user_answers.filter(answer='uncertain')

    return render(request, template, {
        'correct_percentage': correct_percentage,
        'incorrect_percentage': incorrect_percentage,
        'uncertain_percentage': uncertain_percentage,
        'incorrect_questions': incorrect_questions,
        'uncertain_questions': uncertain_questions
    })


def reset_answers(request):
    UserAnswer.objects.filter(test__user=request.user).delete()
    return redirect('questions:questions')
