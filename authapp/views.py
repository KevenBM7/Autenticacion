from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .encriptacion import validatePassword, cryptPassword
from .forms import LoginForm, RegisterForm
#se agregaron estos dos
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

# Vista para el inicio de sesión
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form.is_valid():  
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']  
            
            try:
                user = User.objects.get(email=email)  # Buscar el usuario por email
                if validatePassword(password, user.password):
                    # si inica sesión correctamente
                    #crear sesión "cookie"
                    #agregar los datos que necesito
                    request.session['user.id'] = user.id
                    request.session['user.name'] = email
                    
                    #agregar la duracion (tiempo en seg)
                    request.session.set_expiry(3600)
                    
                    #return al dashboard
                    return redirect('dashboard')  # Redirigir a dashboard.html si el login es exitoso
                else:
                    return render(request, "error.html", {"error": "Contraseña incorrecta"})  # Mostrar error si la contraseña es incorrecta
            except User.DoesNotExist:
                return render(request, "error.html", {"error": "Usuario no encontrado"})
    else:
        form = LoginForm()  # Crear un formulario vacío si no es una solicitud POST
    
    return render(request, "login.html", {'form': form})  # Renderizar la plantilla de login con el formulario

# Vista para el registro de usuario
def register_view(request):
    form = RegisterForm()  # Inicializar el formulario aquí para todas las solicitudes
    if request.method == "POST":
        form = RegisterForm(request.POST) 
        if form.is_valid():  
            email = form.cleaned_data['email']  
            password = form.cleaned_data['password']  
            role = form.cleaned_data['role']  
            
            encrypted_password = cryptPassword(password) 
            User.objects.create(email=email, password=encrypted_password, role=role)  
            return redirect('login')  
    
    return render(request, "register.html", {'form': form})  # Renderizar el formulario

def dashboard_view(request):
        user_id = request.user_id
        usuario = request.usuario
        return HttpResponse(f'Bienbenido {usuario} Su ID es{user_id}')
    
def logout_view(request):
    logout (request)
    return redirect('login')

