from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
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