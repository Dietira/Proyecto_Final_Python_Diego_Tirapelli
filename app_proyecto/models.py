from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    usuario =models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"Usuario: {self.usuario.username} -- Direccion: {self.imagen}"

class Raza(models.Model):
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    tamanio_promedio = models.CharField(max_length=50)
    esperanza_de_vida = models.IntegerField()
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Mascota(models.Model):
    TIPO = [('PERRO', 'Perro'),('GATO', 'Gato'),('OTRO', 'Otro'),]
    nombre = models.CharField(max_length=50)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='fotos', null=True, blank=True, default=None)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} -- Raza:{self.raza.nombre}'
     
class Mascotas_Favoritas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f'Usuario: {self.usuario.nombre} -- Raza:{self.mascota.nombre}'

class Solicitud_Adopcion(models.Model):
    ESTADOS = [('PROCESANDO', 'Procesando'),('FINALIZADA', 'Finalizada'),('RECHAZADA', 'Rechazada'),]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add= True)
    fecha_cambio_estado = models.DateField(auto_now_add= True)
    mensaje = models.TextField() 
    respuesta = models.TextField(default='') 
    estado = models.CharField(max_length=12, choices=ESTADOS, default='PROCESANDO')

