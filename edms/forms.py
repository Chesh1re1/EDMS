from django import forms
from .models import Doc
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ['number', 'title', 'id_contr', 'reg_surname', 'reg_name', 'reg_patronymic', 'id_executor', 'comment']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'id_contr': forms.Select(attrs={'class': 'form-control'}),
            'reg_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_name': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'id_executor': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
