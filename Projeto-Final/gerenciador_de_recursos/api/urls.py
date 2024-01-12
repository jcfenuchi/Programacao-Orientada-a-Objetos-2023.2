from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('get_info', views.getdata),
    path('last_host', views.last_minutes_hostname),
    path('send/', views.addItem)
]
