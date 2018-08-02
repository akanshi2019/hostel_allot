from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegistrationForm

def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
        else:
            return HttpResponse("<h1>invalid form</h1>")
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)