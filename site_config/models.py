from django.db import models

class SiteConfiguration(models.Model):
    hero_title = models.TextField("Título Principal (Hero)", default="Resultados Reales. <br> <span class='brand-red'>Con un Entrenamiento Real.</span>")
    hero_subtitle = models.TextField("Subtítulo (Hero)", default="Deja de adivinar en el gimnasio...")
    hero_button_text = models.CharField("Texto del Botón (Hero)", max_length=100, default="Empezar mi Transformación")
    hero_background_image = models.ImageField("Imagen de Fondo (Hero)", upload_to='site_images/', blank=True, null=True)
    
    routines_title = models.CharField("Título (Sección Rutinas)", max_length=200, default="RUTINAS <span class='brand-red'>GRATUITAS</span>")
    routines_description = models.TextField("Descripción (Sección Rutinas)", default="Empieza a moverte...")
    
    cta_title = models.CharField("Título (Sección CTA)", max_length=200, default="¿LISTO PARA UN <span class='brand-red'>CAMBIO REAL?</span>")
    cta_description = models.TextField("Descripción (Sección CTA)", default="Mi plan de entrenamiento personalizado...")
    cta_features = models.TextField("Características (Sección CTA)", help_text="Una característica por línea.", default="Planificación 100% adaptada a ti.\nAumento de masa muscular...")
    cta_button_text = models.CharField("Texto del Botón (CTA)", max_length=100, default="¡Contactar por WhatsApp!")
    cta_background_image = models.ImageField("Imagen de Fondo (CTA)", upload_to='site_images/', blank=True, null=True)

    nutrition_title = models.CharField("Título (Sección Nutrición)", max_length=200, default="NUTRICIÓN <span class='brand-red'>INTELIGENTE</span>")
    nutrition_description = models.TextField("Descripción (Sección Nutrición)", default="El 70% de tus resultados se logran en la cocina...")
    
    blog_title = models.CharField("Título (Sección Blog)", max_length=200, default="BLOG: CONOCIMIENTO <span class='brand-red'>ES PODER</span>")
    blog_description = models.TextField("Descripción (Sección Blog)", default="Mantente actualizado...")
    
    about_image = models.ImageField("Imagen (Acerca de Mí)", upload_to='site_images/', blank=True, null=True)
    about_title = models.CharField("Título (Acerca de Mí)", max_length=200, default="SOY <span class='brand-red'>BREYNER RIVEROS</span>")
    about_subtitle = models.CharField("Subtítulo (Acerca de Mí)", max_length=200, default="Tu Coach y Aliado en esta Transformación.")
    about_text = models.TextField("Texto Principal (Acerca de Mí)", default="Mi pasión por el fitness va más allá de levantar pesas...")
    about_button_text = models.CharField("Texto del Botón (Acerca de Mí)", max_length=100, default="Contáctame por WhatsApp")
    
    whatsapp_number = models.CharField("Número de WhatsApp", max_length=20, default="573133560878", help_text="Solo números, sin el '+'")
    instagram_url = models.URLField("URL de Instagram", default="#")
    tiktok_url = models.URLField("URL de TikTok", default="#")
    facebook_url = models.URLField("URL de Facebook", default="#")

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteConfiguration, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs): pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuraciones del Sitio"