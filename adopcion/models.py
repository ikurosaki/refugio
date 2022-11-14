from django.db import models

# Create your models here.

# Modelo Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return self.nombre
   

# Modelo Mascota
# null=True:  Permite valores nulo en la base de datos
# blank=True: Permite guardar sin haber ingresado ningun en ese campo
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    # persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    persona = models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField('Vacuna')
    
    def __str__(self):
        return self.nombre    


# Modelo Vacuna
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Modelo Solicitud
class Solicitud(models.Model):
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    persona = models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)