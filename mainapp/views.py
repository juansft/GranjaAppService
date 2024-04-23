from django.shortcuts import render
from productos.models import Producto, CategoriaProducto
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):

  categorias = CategoriaProducto.objects.all()
  productos = Producto.objects.filter(publico=True)
  cattmp = Producto.objects.filter(categoria=1)
  
  return render(request, 'mainapp/index.html', {
    'titulo':'Home',
    'categorias':categorias,
    'productos':productos,
    'cattmp':cattmp
  })
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir al usuario a la pantalla principal después del registro exitoso
            return redirect('pantalla_principal')  # Cambia 'pantalla_principal' por el nombre de tu URL
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})