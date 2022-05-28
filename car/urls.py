from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('cars/', views.cars, name="car"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('book-car/', views.bookCar, name="book-car"),
    path('search/', views.search, name="search"),
    path('cars/details/<str:pk>', views.details, name="details"),
    path('cars/details/book/<str:pk>', views.book, name="book"),
]