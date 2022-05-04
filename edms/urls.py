from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('doc/', AllDoc.as_view(), name='doc'),
    path('dep/', AllDep.as_view(), name='dep'),
    path('contr/', AllContr.as_view(), name='contr'),
    path('add_doc/', AddDoc.as_view(), name='add_doc'),
    path('', Index.as_view(), name='index')
]