from django.shortcuts import render, redirect
from .forms import SzkolenieForm, KategoriaForm, RejestracjaForm

# PANEL
def panel(request):
    return render(request, 'panel.html')

# LISTY (na razie proste)
def categ_list(request):
    return render(request, 'categ_list.html')

def course_list(request):
    return render(request, 'course_list.html')

# DODAJ KATEGORIĘ
def categ_add(request):
    if request.method == 'POST':
        form = KategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/offer-mng/categ-lst')
    else:
        form = KategoriaForm()

    return render(request, 'categ_add.html', {'form': form})

# DODAJ SZKOLENIE
def course_add(request):
    if request.method == 'POST':
        form = SzkolenieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/offer-mng/course-lst')
    else:
        form = SzkolenieForm()

    return render(request, 'course_add.html', {'form': form})

# REJESTRACJA
def register(request):
    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/offer')
    else:
        form = RejestracjaForm()

    return render(request, 'register.html', {'form': form})

from django.http import JsonResponse
from .models import Kategoria, Szkolenie, Rejestracja

def api_categories(request):
    data = list(Kategoria.objects.values())
    return JsonResponse(data, safe=False)


def api_courses(request):
    data = list(Szkolenie.objects.values())
    return JsonResponse(data, safe=False)


def api_registers(request):
    data = list(Rejestracja.objects.values())
    return JsonResponse(data, safe=False)