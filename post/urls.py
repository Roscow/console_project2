from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('proyectos', views.proyectos_list, name='proyectos_list'),
    path('programadores', views.programadores_list, name='programadores_list'),
]
