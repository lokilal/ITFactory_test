from rest_framework.viewsets import ModelViewSet

from .models import SalesPoint
from .serializers import SalesPointSerializer


class SalesPointViewSet(ModelViewSet):
    queryset = SalesPoint.objects.all()
    serializer_class = SalesPointSerializer
