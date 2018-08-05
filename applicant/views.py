from django.shortcuts import render
from django.http import HttpResponseRedirect

from applicant.models import allot
from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            your_name = form.cleaned_data['your_name']
            user = allot.objects.get(your_name=your_name)
            up = allot.objects.get(user=user)
            up.your_name = your_name
            up.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'hostel/name.html', {'form': form})