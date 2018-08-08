from django.shortcuts import render, redirect
from django.http import HttpResponse

from applicant.models import Allot
from .forms import AlotForm

def get_name(request):
    if request.method == 'POST':
        form = AlotForm(request.POST)
        if form.is_valid():
            allotment = form.save(commit=False)
            allotment.save()
            return render(request, 'hostel/home.html')
    else:
        form = AlotForm()
    return render(request, 'hostel/name.html', {'form': form})
