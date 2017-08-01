from django.shortcuts import render, redirect
from .forms import RegistrationForm
from email_hunter import EmailHunterClient

def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = "Marko Petkovic"

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            client = EmailHunterClient('18c8c0f231fb70655152e81e54bb37004a304c0a')
            if client.exist(email):
                form.save()
                return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)