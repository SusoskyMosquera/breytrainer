from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

def post_detail_view(request, post_id):
    return TemplateView.as_view(template_name='post_detail.html')(request)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/config/', include('site_config.urls')),
    
    # Ruta genérica para cualquier tipo de publicación
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
    
    path('', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)