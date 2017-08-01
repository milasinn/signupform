from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import clearbit


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        clearbit.key = 'sk_ee2752f0284b4d36b879bc73326285b7'
        response = clearbit.Enrichment.find(email=user.email, stream=True)
        user.clearbit_data = response
        if commit:
            user.save()

        return user