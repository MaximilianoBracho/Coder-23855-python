from django.urls import path
from ManageCompany.models import Concesionaria,Empelado,Direccion
from ManageCompany import views

urlpatterns = [
    path('concesionaria-alta/',views.concesionaria_alta),
    path('concesionaria-modificacion/',views.concesionaria_modificacion),
    path('concesionaria-baja/',views.concesionaria_baja),
    path('concesionaria-alta/',views.empleado_alta),
    path('concesionaria-modificacion/',views.empleado_modificacion),
    path('concesionaria-baja/',views.empleado_baja),
        path('concesionaria-alta/',views.direccion_alta),
    path('concesionaria-modificacion/',views.direccion_modificacion),
    path('concesionaria-baja/',views.direccion_baja),
]