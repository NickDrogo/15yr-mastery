"""Define URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single pizza

    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]

