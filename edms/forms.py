from django import forms
from .models import Dep, Contr
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class DocForm(forms.Form):
    number = forms.IntegerField(label='Номер')
    title = forms.CharField(label='Название')
    id_executor = forms.ModelChoiceField(queryset=Contr.objects.all(), label='Контрагент')
    reg_surname = forms.CharField(max_length=255, label='Фамилия регистратора')
    reg_name = forms.CharField(max_length=255, label='Имя регистратора')
    reg_patronymic = forms.CharField(max_length=255, label='Отчество регистратора')
    id_contr = forms.ModelChoiceField(queryset=Dep.objects.all(), label='Исполнитель')
