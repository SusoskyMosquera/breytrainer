from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    POST_TYPE_CHOICES = [
        ('BLOG', 'Blog'),
        ('RUTINA', 'Rutina'),
        ('NUTRICION', 'Nutrición'),
    ]

    post_type = models.CharField("Tipo de Publicación", max_length=10, choices=POST_TYPE_CHOICES, default='BLOG')
    title = models.CharField("Título", max_length=200)
    image = models.ImageField("Imagen Principal", upload_to='post_images/')
    
    # Campos que ahora son más genéricos
    description = models.TextField("Descripción Corta / Resumen", blank=True, help_text="Un resumen que se muestra en la página principal.")
    content = RichTextField("Contenido Completo", blank=True, null=True, help_text="El contenido detallado de la publicación.")
    video = models.FileField("Video", upload_to='post_videos/', blank=True, null=True, help_text="Opcional: solo para Rutinas.")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return f"[{self.get_post_type_display()}] {self.title}"

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-created_at']
