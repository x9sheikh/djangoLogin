from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location = forms.CharField(required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', 'location' )


