from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SiteConfiguration
from .serializers import SiteConfigurationSerializer

class SiteConfigurationAPIView(APIView):
    def get(self, request):
        config = SiteConfiguration.load()
        serializer = SiteConfigurationSerializer(config)
        return Response(serializer.data)