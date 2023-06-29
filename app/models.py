from django.db import models

class Usuario(models.Model):
    usuario             = models.CharField(primary_key=True, max_length=20)
    nombre              = models.CharField(max_length=20)
    apellido_paterno    = models.CharField(max_length=20)
    correo              = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    telefono            = models.CharField(max_length=45)
    contraseña          = models.CharField(max_length=20)    

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)



class Producto(models.Model):

    codigo              = models.IntegerField()
    nombre              = models.CharField(max_length=20)
    precio              = models.IntegerField()
    descripcion         = models.TextField()
    imagen              = models.ImageField(upload_to="productos", null=True)  

    def __str__(self):
        return self.nombre 


opciones_contacto =[
    [0,"Sugerencias"],
    [1,"Informar un problema"],
    [2,"Reclamar"]
]

class Contacto (models.Model):
    tipo_consulta       = models.IntegerField(primary_key=True, choices=opciones_contacto)
    nombre              = models.CharField(max_length=200)
    correo              = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    mensaje             = models.TextField()

    def __str__(self):
        return self.nombre 
    
    


class Fierros(models.Model):
    codigo              = models.CharField(primary_key=True, max_length=20)
    nombre              = models.CharField(max_length=20)
    tipo                = models.CharField(max_length=20)
    precio              = models.CharField(max_length=45)
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.tipo)
    
