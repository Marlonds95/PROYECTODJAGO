from django.db import models

# Create your models here.

class Social(models.Model):
    key = models.SlugField(max_length=50, unique=True, verbose_name="Clave")
    name = models.CharField(max_length=50, verbose_name="Red Social")
    url = models.URLField(null=True, blank=True, verbose_name="Enlace")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name="enlace"
        verbose_name_plural="enlaces"
        ordering=['name']

    def __str__(self):
        return self.name