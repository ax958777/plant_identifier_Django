from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('identify/', views.identify_plant, name='identify_plant'),
]