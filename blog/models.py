from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre categoría")  # Corregir aquí
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")  # Corregir aquí
    published = models.DateTimeField(default=timezone.now, verbose_name="Fecha de publicación")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="blog", verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    category = models.ManyToManyField(Category, verbose_name="Categorias")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title