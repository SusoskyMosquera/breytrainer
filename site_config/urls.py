from django.urls import path
from .views import SiteConfigurationAPIView

urlpatterns = [
    path('', SiteConfigurationAPIView.as_view(), name='site-configuration'),
]
