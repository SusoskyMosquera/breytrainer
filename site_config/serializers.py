from rest_framework import serializers
from .models import SiteConfiguration

class SiteConfigurationSerializer(serializers.ModelSerializer):
    hero_background_image = serializers.ImageField(use_url=True, required=False)
    cta_background_image = serializers.ImageField(use_url=True, required=False)
    about_image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = SiteConfiguration
        fields = '__all__'
