from django.urls import path, include
from .views import index

urlpatterns = [

    path ('cursos/', index, name='index'),

]
