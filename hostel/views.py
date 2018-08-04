from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from hostel.models import UserProfile
from .forms import RegistrationForm


def home(request):
    return render(request, 'accounts/home.html')



def register(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>welcome</h1>")
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                first_name = form.cleaned_data['first_name']
                fathers_name = form.cleaned_data['fathers_name']
                course = form.cleaned_data['course']
                technology = form.cleaned_data['technology']
                #email = form.cleaned_data['email']
                role= form.cleaned_data['role']
                user=User.objects.get(first_name=first_name)
                up=UserProfile.objects.get(user=user)
                up.fathers_name=fathers_name
                up.course=course
                up.technology=technology
                up.role=role
                up.save()
                return HttpResponse("<h1>registered, now try to login</h1>")
            else:
                return HttpResponse("<h1>invalid form</h1>")
        else:
            form = RegistrationForm()
            args = {'form': form}
            return render(request,'accounts/reg_form.html',args)
