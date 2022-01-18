from django.shortcuts import render
from django.http import HttpResponse
from ManageCompany.models import Concesionaria,Empelado,Direccion

# Create your views here.
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
