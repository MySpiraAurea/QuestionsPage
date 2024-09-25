from django.shortcuts import redirect, render
from .forms import RegistrationForm


def registration(request):
    template = 'registration/registration.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:login')  # Перенаправление на страницу логина после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, template, {'form': form})

