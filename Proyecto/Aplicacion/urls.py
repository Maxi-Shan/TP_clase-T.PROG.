from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('registrar-prestamo/', views.registrar_prestamo, name='registrar_prestamo'),
    path('libros-por-categoria/<int:categoria_id>/', views.libros_por_categoria, name='libros_por_categoria'),
    path('actualizar-devolucion/<int:prestamo_id>/', views.actualizar_devolucion, name='actualizar_devolucion'),
]
