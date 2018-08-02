from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

choices=[
    ('applicant','Applicant'),
    ('executive','Executive'),
]
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    fathers_name = forms.CharField(max_length=30, required=False)
    course= forms.CharField(max_length=30, required=False)
    technology = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    applicant_or_executive= forms.CharField(label=' Applicant or Executive',widget=forms.Select(choices=choices))
    class Meta:
        model=User
        fields = [
            'username',
            'first_name',
            'last_name',
            'fathers_name',
            'course',
            'technology',
            'email',
            'applicant_or_executive',
            'password1',
            'password2',
        ]


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.fathers_name = self.cleaned_data['fathers_name']
        user.course = self.cleaned_data['course']
        user.technology = self.cleaned_data['technology']
        user.email = self.cleaned_data['email']
        user.applicant_or_executive = self.cleaned_data[' applicant_or_executive']
        if commit:
            user.save()
        return user