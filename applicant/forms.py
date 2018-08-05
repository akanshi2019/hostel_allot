from django import forms

from applicant.models import allot


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100,widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'name',}))

    class Meta:
        model = allot
        fields = [
            'your_name',

        ]
    def save(self, commit=True):
        user = super(NameForm, self).save(commit=False)
        user.first_name = self.cleaned_data['your_name']
        if commit:
            user.save()
        return user