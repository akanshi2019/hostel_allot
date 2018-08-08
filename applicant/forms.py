from django import forms
from django.contrib.auth.models import User

from applicant.models import Allot


class AlotForm(forms.ModelForm):

    class Meta:
        model = Allot
        fields = [
            'first_name',
        ]

