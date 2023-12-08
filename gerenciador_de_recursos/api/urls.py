from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata),
    path('send/', views.addItem)
]
