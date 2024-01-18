from django.db import models
from ckeditor.fields import RichTextField
class Feature(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    published = models.DateField(verbose_name="Fecha de estreno")
    videotitle = models.CharField(max_length=100, verbose_name="T´tulo Video")
    content = RichTextField(verbose_name="Contenido")
    url = models.URLField(null=True, blank=True, verbose_name='URL VIDEO')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "estreno"
        verbose_name_plural = "estrenos"
        ordering = ['-created']

    def __str__(self):
        return self.title

