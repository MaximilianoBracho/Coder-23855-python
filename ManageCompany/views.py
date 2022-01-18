from django.shortcuts import render
from django.http import HttpResponse
from ManageCompany.models import Concesionaria,Empelado,Direccion

# Create your views here.

def ManageCompany(self):
      
    return HttpResponse(f'Portal de Administración de Empresas')


def concesionaria_alta(self):
    
    concesionaria = Concesionaria(
        
    )
    
    return HttpResponse(f'Se ha dado de alta la concesionaria {concesionaria.razon_social}!')

def concesionaria_modificacion(self):
    
    concesionaria = Concesionaria(
        
    )
    
    return HttpResponse(f'Se ha modificado la concesionaria {concesionaria.razon_social}!')

def concesionaria_baja(self):
    
    concesionaria = Concesionaria(
        
    )
    
    return HttpResponse(f'Se ha eliminado la concesionaria {concesionaria.razon_social}!')

def empleado_alta(self):
    
    empleado = Empelado(
        
    )
    
    return HttpResponse(f'Se ha dado de alta el empleado {empleado.dni}!')

def empleado_modificacion(self):
    
    empleado = Empelado(
        
    )
    
    return HttpResponse(f'Se ha modificado el empleado {empleado.dni}!')

def empleado_baja(self):
    
    empleado = Empelado(
        
    )
    
    return HttpResponse(f'Se ha eliminado el empleado {empleado.dni}!')

def direccion_alta(self):
    
    direccion = Direccion(
        
    )
    
    return HttpResponse(f'Se ha dado de alta la direccion {direccion.direccionId}!')

def direccion_modificacion(self):
    
    direccion = Direccion(
        
    )
    
    return HttpResponse(f'Se ha modificado la direccion {direccion.direccionId}!')

def direccion_baja(self):
    
    direccion = Direccion(
        
    )
    
    return HttpResponse(f'Se ha eliminado la direccion {direccion.direccionId}!')

