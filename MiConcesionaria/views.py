from cgitb import html
from django.http import HttpResponse
from django.template import Context, Template, loader

def home(request):
    
    datos = {}
    
    plantilla = loader.get_template('home.html')
    pagina = plantilla.render(datos)
        
    return HttpResponse(pagina)