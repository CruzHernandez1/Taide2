from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Informacion_Usuario(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido_paterno = models.CharField(max_length = 30)   
    apellido_materno = models.CharField(max_length = 30)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length = 100)
    correo_electronico = models.CharField(max_length = 30)
    telefono_contacto = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno + " - " + self.user.username
    
class Picina(models.Model):
    nombre = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 100)
    costo_hora = models.FloatField()
    imagen = models.ImageField(upload_to="images",null = False, blank = False)
    descripcion = models.TextField(max_length = 300)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre + ' - ' + self.user.username

class Galeria_picina(models.Model):
    imagen = models.ImageField(upload_to="images",null = False, blank = False)
    descripcion = models.CharField(max_length = 100)
    picina = models.ForeignKey(Picina, on_delete = models.CASCADE)
    def __str__(self):
        return self.descripcion + " - " + self.picina.nombre

class Paquete_picina(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.TextField(max_length = 300)
    precio = models.FloatField()
    picina = models.ForeignKey(Picina, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre + " - " + self.picina.nombre

    
class Añadido_paquete_picina(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 100)
    precio = models.FloatField()
    picina = models.ForeignKey(Picina, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre + " - " + self.picina.nombre

class Suministro_picina(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length =  100)
    cantidad_inventario =  models.IntegerField()
    picina = models.ForeignKey(Picina, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre + " - " + self.picina.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 100)
    telefono_contacto = models.CharField(max_length = 20)
    correo_electronico = models.CharField(max_length = 30)
    picina = models.ForeignKey(Picina, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre + " - " + self.picina.nombre

class Contrato_texto(models.Model):
    texto = models.TextField(max_length = 500)
    picina = models.ForeignKey(Picina, on_delete = models.CASCADE)
    def __str__(self):
        return "Contrato de la picina: " + self.picina.nombre

class Contrato_rentado(models.Model):
    contenido = models.TextField(max_length=1000)
    cliente = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    rentero = models.IntegerField()
    def _str_(self):
        return "Contrato firmado por " + self.cliente + " con " + self.rentero 
