
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('multidb/',views.combinated_forms_view,name='combinateddb'),
    path('sucess_url/',views.sucess_url,name="sucess")
]


