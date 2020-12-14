from django.shortcuts import render
from django.http import HttpResponse
from .models import *


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
