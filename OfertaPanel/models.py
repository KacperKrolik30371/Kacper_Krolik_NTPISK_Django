from django.db import models

# Kategorie
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    publikuj = models.BooleanField(default=True)
    kolejnosc = models.IntegerField(default=0)
    kategoria_nadrzedna = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nazwa


# Szkolenie
class Szkolenie(models.Model):
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    publikuj = models.BooleanField(default=True)
    kolejnosc = models.IntegerField(default=0)
    liczba_godzin = models.IntegerField()
    numer = models.CharField(max_length=50)
    cena = models.FloatField()

    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.tytul


# Rejestracja
class Rejestracja(models.Model):
    szkolenie = models.ForeignKey(Szkolenie, on_delete=models.CASCADE)
    zgoda_rodo = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    data_rejestracji = models.DateTimeField(auto_now_add=True)

    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"