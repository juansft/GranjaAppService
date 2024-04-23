# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def ingreso(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            # Redirigir al usuario a alguna página de inicio después de iniciar sesión
            return redirect('inicio')
        else:
            # El usuario no está autenticado, puedes agregar un mensaje de error aquí si lo deseas
            pass

    return render(request, 'ingreso.html')

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        # Verificar si el correo ya está registrado
        if User.objects.filter(email=correo).exists():
            # Puedes agregar un mensaje de error indicando que el correo ya está en uso
            pass
        else:
            # Crear el nuevo usuario
            user = User.objects.create_user(username=correo, email=correo, password=contrasena, first_name=nombre, last_name=apellido)
            # Realizar otras acciones necesarias, como enviar un correo de verificación, etc.
            # Aquí se redirige al usuario después de registrarse
            return redirect('ingreso')

    return render(request, 'registro.html')


