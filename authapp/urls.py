from django.urls import path
from django.views.generic import TemplateView  # Importar TemplateView para la vista del dashboard
from .views import login_view, register_view
from django.http import HttpResponse
from django.contrib.auth import logout
from .views import logout_view


urlpatterns = [
    path('login/', login_view, name='login'),  # Ruta para la vista de login
    path('register/', register_view, name='register'),  # Ruta para la vista de registro
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),  # Ruta para el dashboard
    path('logout/', logout_view, name='logout'),# Ruta para el logout
]