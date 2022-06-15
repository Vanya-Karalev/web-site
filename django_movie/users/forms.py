from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegisterForm(UserCreationForm):
    """Registration form"""
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat_Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class UserUpdateForm(UserChangeForm):
    """Change info account form"""
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'id': 'INPUT_19'}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'id': 'INPUT_19'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'id': 'INPUT_19'}))

    class Meta:
        model = User
        fields = ['email',
                  'first_name',
                  'last_name',
                  ]
        widgets = {
            'email': forms.EmailInput(attrs={'id': 'INPUT_19'}),
            'first_name': forms.TextInput(attrs={'id': 'INPUT_19'}),
            'last_name': forms.TextInput(attrs={'id': 'INPUT_19'}),
        }
