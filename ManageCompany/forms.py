from django import forms

class ConcesionariaFormulario(forms.Form):
    
    cuit=forms.CharField(max_length=11)   
    razon_social=forms.CharField(max_length=100)
    nombre_fantasia=forms.CharField(max_length=100)
    fecha_inscripcion=forms.DateField()
    direccion_fiscal=forms.CharField(max_length=100)
    direccion_envio=forms.CharField(max_length=100)
    telefono=forms.CharField(max_length=20)
    email=forms.EmailField()
    fecha_creacion=forms.DateField()
    
class EmpleadoFormulario(forms.Form):
    
    cuil=forms.CharField(max_length=11)
    dni=forms.IntegerField()
    nombres=forms.CharField(max_length=50)
    apellidos=forms.CharField(max_length=50)
    fecha_nacimiento=forms.DateField()
    domicilio=forms.CharField(max_length=100)
    telefono=forms.CharField(max_length=20)
    celular=forms.CharField(max_length=20)
    cargo=forms.CharField(max_length=50)
    email=forms.EmailField()
    companiaId=forms.IntegerField()
    fecha_creacion=forms.DateField()
    
class DireccionFormulario(forms.Form):
    
    pais=forms.CharField(max_length=50)
    provincia=forms.CharField(max_length=50)
    ciudad=forms.CharField(max_length=50)
    codigo_postal=forms.IntegerField()