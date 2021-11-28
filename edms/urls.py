from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register),
    path('login/', user_login),
    path('logout/', user_logout, name='logout'),
    path('doc/', doc),
    path('dep/', dep),
    path('contr/', contr),
    path('add_doc/', add_doc),
    path('', index)
]