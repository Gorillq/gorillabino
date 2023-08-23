from django.urls import path
from . import views

urlpatterns = [
    path('', views.query, name="query"),
    path('', views.results, name="results"),
    path('', views.about, name="about"),
]