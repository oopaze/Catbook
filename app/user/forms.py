from django import forms
from tabelas.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_superuser', )

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Email', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Email ou Username', 'autofocus':True}
        )
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Senha'}
        ),
    )
