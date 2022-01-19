from django.urls import path
from ManageCompany import views

urlpatterns = [
    path('',views.managecompany),
    path('concesionaria_listar/',views.concesionaria_listar, name="Ver Concesionarias"),
    path('empleado_listar/',views.empleado_listar, name="Ver Empleados"),
    path('direccion_listar/',views.direccion_listar, name="Ver Direcciones"),
    path('concesionaria_alta/',views.concesionaria_alta, name="Alta de Concesionaria"),
    path('empleado_alta/',views.empleado_alta, name="Alta de Empleado"),
    path('direccion_alta/',views.direccion_alta, name="Alta de Dirección"),
    path('concesionaria_editar/<id_concesionaria>/',views.concesionaria_editar, name="Editar Concesionaria"),
    path('empleado_editar/<id_empleado>/',views.empleado_editar, name="Editar Empleado"),
    path('direccion_editar/<id_direccion>/',views.direccion_editar, name="Editar Dirección"),
    path('concesionaria_eliminar/<id_concesionaria>/',views.concesionaria_eliminar, name="Eliminar Concesionaria"),
    path('empleado_eliminar/<id_empleado>/',views.empleado_eliminar, name="Eliminar Empleado"),
    path('direccion_eliminar/<id_direccion>/',views.direccion_eliminar, name="Eliminar Dirección"),
]