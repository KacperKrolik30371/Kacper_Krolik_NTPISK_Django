from django.urls import path
from . import views

urlpatterns = [
    path('offer-mng', views.panel),
    path('offer-mng/categ-lst', views.categ_list),
    path('offer-mng/course-lst', views.course_list),
    path('offer-mng/categ-add', views.categ_add),
    path('offer-mng/course-add', views.course_add),
    path('register', views.register),
    path('categories', views.api_categories),
    path('courses', views.api_courses),
    path('registers', views.api_registers),
]