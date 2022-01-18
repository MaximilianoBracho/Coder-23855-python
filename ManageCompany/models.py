from django.db import models

# Create your models here.
class Concesionaria(models.Model):
 
    concesionariaId=id
    cuit=models.CharField('cuit',max_length=11)   
    razon_social=models.CharField('razon social',max_length=100)
    nombre_fantasia=models.CharField('nombre de fantasia',max_length=100)
    fecha_inscriocion=models.DateField('01/01/1990', auto_now=False, auto_now_add=False)
    direccion_fiscal=models.CharField('direccion fiscal',max_length=100)
    direccion_envio=models.CharField('direccion envio',max_length=100)
    telefono=models.CharField('telefono',max_length=20)
    emai=models.EmailField()
    fecha_creacion=models.DateField(auto_now_add=True)
    activo=models.BooleanField()

class Empelado(models.Model):
    
    empleadoId=id
    cuil=models.CharField('cuil',max_length=11)
    dni=models.IntegerField()
    nombres=models.CharField('nombres',max_length=50)
    apellidos=models.CharField('apellidos',max_length=50)
    fecha_nacimiento=models.DateField('01/01/1990', auto_now=False, auto_now_add=False)
    domicilio=models.CharField('domicilio',max_length=100)
    telefono=models.CharField('telefono',max_length=20)
    celular=models.CharField('celular',max_length=20)
    cargo=models.CharField('cargo',max_length=50)
    email=models.EmailField()
    companiaId=models.IntegerField()
    fecha_creacion=models.DateField(auto_now_add=True)
    activo=models.BooleanField()
    
    
class Direccion(models.Model):
    
    direccionId=id
    pais=models.CharField('pais',max_length=50)
    provincia=models.CharField('provincia',max_length=50)
    ciudad=models.CharField('ciudad',max_length=50)
    codigo_postal=models.IntegerField()
    
    
