from django.shortcuts import render, redirect
from .forms import LibroForm, PrestamoForm
from .models import Categoria, Libro, Prestamo

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

def registrar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'registrar_prestamo.html', {'form': form})

def libros_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    libros = Libro.objects.filter(categoria=categoria)
    return render(request, 'libros_por_categoria.html', {'categoria': categoria, 'libros': libros})

def actualizar_devolucion(request, prestamo_id):
    prestamo = Prestamo.objects.get(id=prestamo_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'actualizar_devolucion.html', {'form': form})



def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')