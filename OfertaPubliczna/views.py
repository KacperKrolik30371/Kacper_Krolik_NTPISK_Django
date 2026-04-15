from django.shortcuts import render

from django.http import HttpResponse

def kategorie(request):
    return HttpResponse("<h1>Kategorie (publiczne)</h1>")

def lista_szkolen(request, kategoria):
    return HttpResponse(f"<h1>Szkolenia: {kategoria}</h1>")

def szczegoly(request, kategoria):
    return HttpResponse(f"<h1>Szczegóły szkolenia: {kategoria}</h1>")
