from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def doc(request):
    doc = Doc.objects.order_by('-doc_reg_date')
    return render(request, 'edms/doc.html', {'doc': doc, 'title': 'Список документов'})


def contr(request):
    contr = Contr.objects.all()
    return render(request, 'edms/contr.html', {'contr': contr, 'title': 'Список контрагентов'})


def dep(request):
    dep = Dep.objects.all()
    return render(request, 'edms/dep.html', {'dep': dep, 'title': 'Список исполнителей'})
