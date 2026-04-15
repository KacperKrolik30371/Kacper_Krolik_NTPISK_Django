Projekt Django – System Szkoleniowy

Projekt wykonany w ramach zajęć Nowoczesne aplikacje internetowe.
Aplikacja umożliwia zarządzanie szkoleniami, kategoriami oraz rejestrację użytkowników.

---

Wymagania:

* Python 3.x
* pip
* Django

---

Uruchomienie projektu:

1. Pobierz repozytorium:
   git clone https://github.com/KacperKrolik30371/Kacper_Krolik_NTPISK_Django.git

2. Przejdź do folderu projektu:
   cd Djangoapp

3. Zainstaluj Django:
   pip install django

4. Wykonaj migracje:
   python manage.py migrate

5. Uruchom serwer:
   python manage.py runserver

---

Dostęp do aplikacji:

Panel główny:
http://127.0.0.1:8000/offer-mng

Aplikacja publiczna:
http://127.0.0.1:8000/offer

Panel admina:
http://127.0.0.1:8000/admin

Formularz dodawania szkolenia:
http://127.0.0.1:8000/offer-mng/course-add

API (JSON):
http://127.0.0.1:8000/categories

---

Funkcjonalności:

* zarządzanie kategoriami i szkoleniami
* rejestracja użytkowników na szkolenia
* panel administracyjny Django
* formularze z zapisem do bazy danych
* endpointy API zwracające dane w formacie JSON

---

Autor:

Kacper Królik
