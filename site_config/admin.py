from django.contrib import admin
from .models import SiteConfiguration

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Impedir que se creen nuevas instancias si ya existe una
        return not SiteConfiguration.objects.exists()
