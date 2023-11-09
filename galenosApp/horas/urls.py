from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('hora/create', views.create_hora, name='hora-create'),
]