# Se screaronn los formularios de registro y login
from django import forms

# Formulario de inicio de sesión
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)  # Campo de email requerido
    password = forms.CharField(widget=forms.PasswordInput, required=True)  # Campo de contraseña con entrada oculta

# Formulario para el registro de usuario
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True) 
    password = forms.CharField(widget=forms.PasswordInput, required=True)  # Campo de contraseña con entrada oculta
    role = forms.ChoiceField(choices=[('user', 'Usuario'), ('admin', 'Administrador')], required=True)  # Selección de rol