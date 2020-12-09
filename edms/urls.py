from django.urls import path
from .views import *


urlpatterns = [
    path('doc/', doc),
    path('dep/', dep),
    path('contr/', contr),
    path('', index)
]