from django.db import models

class Curso(models.Model):
	nombre=models.CharField(max_length=140)
	fecha_inicio=models.DateTimeField()
	descripcion=models.TextField() 
	imagen=models.ImageField(upload_to='cursos/media',blank=True,null=True)

# Create your models here.
