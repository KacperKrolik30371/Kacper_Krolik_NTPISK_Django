from django.urls import path
from . import views

urlpatterns = [
    path('offer', views.kategorie),
    path('offer/<str:kategoria>', views.lista_szkolen),
    path('offer/<str:kategoria>/course', views.szczegoly),
]