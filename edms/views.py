from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def doc(request):
    doc = Doc.objects.order_by('-doc_reg_date')
    return render(request, 'edms/doc.html', {'doc': doc, 'title': 'Список документов'})
