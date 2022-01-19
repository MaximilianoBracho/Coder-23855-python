from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from ManageCompany.forms import ConcesionariaFormulario, EmpleadoFormulario, DireccionFormulario
from ManageCompany.models import Concesionaria,Empleado,Direccion

# Create your views here.

def managecompany(request):
    
    datos = {}
    
    plantilla = loader.get_template('managecompany/managecompany.html')
    pagina = plantilla.render(datos,request)
      
    return HttpResponse(pagina)

def concesionaria_listar(request):
    
    concesionarias = Concesionaria.objects.all()
    contexto = {"concesionarias":concesionarias}
   
    return render(request,"ManageCompany/concesionaria_listar.html",contexto)

def empleado_listar(request):
    
    empleados= Empleado.objects.all()
    contexto = {"empleados":empleados}
   
    return render(request,"ManageCompany/empleado_listar.html",contexto)

def direccion_listar(request):
    
    direcciones = Direccion.objects.all()
    contexto = {"direcciones":direcciones}
   
    return render(request,"ManageCompany/direccion_listar.html",contexto)


def concesionaria_alta(request):
    
    if(request.method == 'POST'):
        
        formulario = ConcesionariaFormulario(request.POST)
        
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
            concesionaria = Concesionaria(
                
                cuit=datos["cuit"],
                razon_social=datos["razon_social"],
                nombre_fantasia=datos["nombre_fantasia"],
                fecha_inscripcion=datos["fecha_inscripcion"],
                direccion_fiscal=datos["direccion_fiscal"],
                direccion_envio=datos["direccion_envio"],
                telefono=datos["telefono"],
                email=datos["email"],
                fecha_creacion=datos["fecha_creacion"],
                activo=True
            )
            
            concesionaria.save()
            
        concesionarias = Concesionaria.objects.all()
        contexto = {"concesionarias":concesionarias}          
            
        return render(request, "managecompany/concesionaria_listar.html",contexto)
            
    else:
            
        formulario = ConcesionariaFormulario()
            
        return render(request, "managecompany/concesionaria_alta.html",{"form": formulario})
    
    
def empleado_alta(request):
    
    if(request.method == 'POST'):
        
        formulario = EmpleadoFormulario(request.POST)
        
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
            empleado = Empleado(
                
                cuil=datos["cuil"],
                dni=datos["dni"],
                nombres=datos["nombres"],
                apellidos=datos["apellidos"],
                fecha_nacimiento=datos["fecha_nacimiento"],
                domicilio=datos["domicilio"],
                telefono=datos["telefono"],
                celular=datos["celular"],
                cargo=datos["cargo"],
                email=datos["email"],
                companiaId=datos["companiaId"],
                fecha_creacion=datos["fecha_creacion"],
                activo=True
            )
            
            empleado.save()
            
        empleados= Empleado.objects.all()
        contexto = {"empleados":empleados}
    
        return render(request,"ManageCompany/empleado_listar.html",contexto)
            
    else:
            
        formulario = EmpleadoFormulario()
            
        return render(request, "managecompany/empleado_alta.html",{"form": formulario})
    
    
def direccion_alta(request):
    
    if(request.method == 'POST'):
        
        formulario = DireccionFormulario(request.POST)
        
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
            direccion = Direccion(
                
                pais=datos["pais"],
                provincia=datos["provincia"],
                ciudad=datos["ciudad"],
                codigo_postal=datos["codigo_postal"]
            )
            
            direccion.save()
            
        direcciones = Direccion.objects.all()
        contexto = {"direcciones":direcciones}
    
        return render(request,"ManageCompany/direccion_listar.html",contexto)
            
    else:
            
        formulario = DireccionFormulario()
            
        return render(request, "managecompany/direccion_alta.html",{"form": formulario})
    
def concesionaria_editar(request,id_concesionaria):
    
    concesionaria = Concesionaria.objects.get(id=id_concesionaria)
    
    if(request.method == 'POST'):
        
        formulario = ConcesionariaFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
                   
            concesionaria.cuit=datos["cuit"]
            concesionaria.razon_social=datos["razon_social"]
            concesionaria.nombre_fantasia=datos["nombre_fantasia"]
            concesionaria.fecha_inscripcion=datos["fecha_inscripcion"]
            concesionaria.direccion_fiscal=datos["direccion_fiscal"]
            concesionaria.direccion_envio=datos["direccion_envio"]
            concesionaria.telefono=datos["telefono"]
            concesionaria.email=datos["email"]
            concesionaria.fecha_creacion=datos["fecha_creacion"]
            concesionaria.activo=True
            
            concesionaria.save()
            
        concesionarias = Concesionaria.objects.all()
        contexto = {"concesionarias":concesionarias}          
            
        return render(request, "managecompany/concesionaria_listar.html",contexto)
            
    else:
            
        formulario = ConcesionariaFormulario(initial={
            'cuit':concesionaria.cuit,
            'razon_social':concesionaria.razon_social,
            'nombre_fantasia':concesionaria.nombre_fantasia,
            'fecha_inscripcion':concesionaria.fecha_inscripcion,
            'direccion_fiscal':concesionaria.direccion_fiscal,
            'direccion_envio':concesionaria.direccion_envio,
            'telefono':concesionaria.telefono,
            'email':concesionaria.email,
            'fecha_creacion':concesionaria.fecha_creacion
        })
            
        return render(request, "managecompany/concesionaria_editar.html",{"form": formulario, "id_concesionaria": concesionaria.id})
    
def empleado_editar(request,id_empleado):
    
    empleado = Empleado.objects.get(id=id_empleado)
    
    if(request.method == 'POST'):
        
        formulario = EmpleadoFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
                   
            empleado.cuil=datos["cuil"]
            empleado.dni=datos["dni"]
            empleado.nombres=datos["nombres"]
            empleado.apellidos=datos["apellidos"]
            empleado.fecha_nacimiento=datos["fecha_nacimiento"]
            empleado.domicilio=datos["domicilio"]
            empleado.telefono=datos["telefono"]
            empleado.celular=datos["celular"]
            empleado.cargo=datos["cargo"]
            empleado.email=datos["email"]
            empleado.companiaId=datos["companiaId"]
            empleado.fecha_creacion=datos["fecha_creacion"]
            
            empleado.save()
            
        empleados= Empleado.objects.all()
        contexto = {"empleados":empleados}
    
        return render(request,"ManageCompany/empleado_listar.html",contexto)
            
    else:
            
        formulario = EmpleadoFormulario(initial={
            "cuil":empleado.cuil,
            "dni":empleado.dni,
            "nombres":empleado.nombres,
            "apellidos":empleado.apellidos,
            "fecha_nacimiento":empleado.fecha_nacimiento,
            "domicilio":empleado.domicilio,
            "telefono":empleado.telefono,
            "celular":empleado.celular,
            "cargo":empleado.cargo,
            "email":empleado.email,
            "companiaId":empleado.companiaId,
            "fecha_creacion":empleado.fecha_creacion
        })
            
        return render(request, "managecompany/empleado_editar.html",{"form": formulario, "id_empleado": empleado.id})
    

def direccion_editar(request,id_direccion):
    
    direccion = Direccion.objects.get(id=id_direccion)
        
    if(request.method == 'POST'):
        
        formulario = DireccionFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
                
            direccion.pais=datos["pais"]
            direccion.provincia=datos["provincia"]
            direccion.ciudad=datos["ciudad"]
            direccion.codigo_postal=datos["codigo_postal"]
            
            direccion.save()
            
        direcciones = Direccion.objects.all()
        contexto = {"direcciones":direcciones}
    
        return render(request,"ManageCompany/direccion_listar.html",contexto)
            
    else:
            
        formulario = DireccionFormulario(initial={
            "pais":direccion.pais,
            "provincia":direccion.provincia,
            "ciudad":direccion.ciudad,
            "codigo_postal":direccion.codigo_postal
        })
            
        return render(request, "managecompany/direccion_editar.html",{"form": formulario, "id_direccion": direccion.id})

def concesionaria_eliminar(request,id_concesionaria):
    
    concesionaria = Concesionaria.objects.get(id=id_concesionaria)
    concesionaria.delete()
    
    concesionarias = Concesionaria.objects.all()
    contexto = {"concesionarias":concesionarias}          
            
    return render(request, "managecompany/concesionaria_listar.html",contexto)

def empleado_eliminar(request,id_empleado):
    
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.delete()
    
    empleados= Empleado.objects.all()
    contexto = {"empleados":empleados}
    
    return render(request,"ManageCompany/empleado_listar.html",contexto)

def direccion_eliminar(request,id_direccion):
    
    direccion = Direccion.objects.get(id=id_direccion)
    direccion.delete()
    
    direcciones = Direccion.objects.all()
    contexto = {"direcciones":direcciones} 
    
    return render(request,"ManageCompany/direccion_listar.html",contexto)