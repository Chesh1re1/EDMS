from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from .forms import DocForm, UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('login')
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
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'edms/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect(user_login)


class AllDoc(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Doc
    template_name = 'edms/doc.html'
    context_object_name = 'doc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doc'] = Doc.objects.order_by('-doc_reg_date')
        return context


class AllDep(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Dep
    template_name = 'edms/dep.html'
    context_object_name = 'dep'


class AllContr(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Contr
    template_name = 'edms/contr.html'
    context_object_name = 'contr'


class AddDoc(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = DocForm
    template_name = 'edms/add_doc.html'


class Index(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Doc
    template_name = 'edms/index.html'
    context_object_name = 'doc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doc'] = Doc.objects.order_by('-doc_reg_date')
        context['contr'] = Contr.objects.order_by('id')
        context['dep'] = Dep.objects.order_by('id')
        context['title'] = 'Полная информация'
        context['doc_title'] = 'Список документов'
        context['dep_title'] = 'Список исполнителей'
        context['contr_title'] = 'Список контрагентов'
        return context

