from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name="index"),
    path('pythonlogics', views.pythonlogics, name="pythonlogics"),
    path('ht_cm/', views.ht_cm_view, name="ht_cm"),
    path('bmi/', views.BMI_view, name="bmi"),
    path('calendar/', views.calendar_view, name="calendar"),
    path('simpleinterest/', views.simpleinterest_view, name="simpleinterest"),
]
