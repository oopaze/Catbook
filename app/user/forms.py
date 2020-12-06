from django import forms
from tabelas.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=255
    )
    username = forms.CharField(
        max_length=50
    )
    password = forms.CharField(
        max_length=255, 
        widget=forms.PasswordInput(
            
        )
    )

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'username', 'password', 'profile_pic', 'data_nascimento', 'genero')

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
