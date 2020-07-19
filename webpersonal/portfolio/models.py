from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description= models.TextField(verbose_name="Descripcion")
    image= models.ImageField(verbose_name="Imagen", upload_to= "projects")
    Direc= models.URLField(null = True,blank = True,verbose_name = "Dirección Web", max_length=200)
    Create= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    update= models.DateTimeField(auto_now=True,verbose_name="Fecha de modificacion")

    class Meta:
      verbose_name = 'proyecto'
      verbose_name_plural = 'proyectos'
      ordering = ["-Create"]    
    def __str__ (self):
        return self.title  