from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import DocForm, UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect(index)
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegistrationForm()
    return render(request, 'edms/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(index)
    else:
        form = UserLoginForm()
    return render(request, 'edms/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect(user_login)


def doc(request):
    doc = Doc.objects.order_by('-doc_reg_date')
    return render(request, 'edms/doc.html', {'doc': doc, 'title': 'Список документов'})


def contr(request):
    contr = Contr.objects.order_by('id')
    return render(request, 'edms/contr.html', {'contr': contr, 'title': 'Список контрагентов'})


def dep(request):
    dep = Dep.objects.order_by('id')
    return render(request, 'edms/dep.html', {'dep': dep, 'title': 'Список исполнителей'})


def index(requst):
    doc = Doc.objects.order_by('-doc_reg_date')
    contr = Contr.objects.order_by('id')
    dep = Dep.objects.order_by('id')
    context = {
        'doc': doc,
        'contr': contr,
        'dep': dep,
        'title': 'Полная информация',
        'doc_title': 'Список документов',
        'dep_title': 'Список исполнителей',
        'contr_title': 'Список контрагентов'
    }
    return render(requst, 'edms/index.html', context=context)


def add_doc(request):
    if request.method == 'POST':
        pass
    else:
        form = DocForm()
    return render(request, 'edms/add_doc.html', {'form': form})
