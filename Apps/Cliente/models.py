from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True,)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.CharField(max_length=1000)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)  # Assuming 'General' has ID 1 in Categoria

    def __str__(self):
        return self.nombre   
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    fecha = models.DateField()
    hora = models.TimeField()
    numero_personas = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente') 
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cliente.nombre + " " + self.fecha.strftime("%Y-%m-%d") + " " + self.hora.strftime("%H:%M")