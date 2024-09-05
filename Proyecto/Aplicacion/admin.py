from django.contrib import admin
from .models import Autor, Libro, Categoria, Prestamo

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(Prestamo)