from django import forms
from .models import Szkolenie, Kategoria, Rejestracja

class SzkolenieForm(forms.ModelForm):
    class Meta:
        model = Szkolenie
        fields = ['numer', 'tytul', 'kategoria', 'liczba_godzin', 'cena', 'kolejnosc', 'publikuj']

class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa', 'kolejnosc', 'publikuj', 'kategoria_nadrzedna']

class RejestracjaForm(forms.ModelForm):
    class Meta:
        model = Rejestracja
        fields = ['szkolenie', 'imie', 'nazwisko', 'telefon', 'email', 'zgoda_rodo']