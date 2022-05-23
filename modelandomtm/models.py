from django.db import models
# se Generara con many-to-many un nueva tabla
class Carrera(models.Model):
    title = models.CharField(max_length=50)
    universidad = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Persona(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    age = models.IntegerField()
    estudios = models.ManyToManyField(Carrera)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.nombre