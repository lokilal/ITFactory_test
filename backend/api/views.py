from rest_framework.viewsets import ModelViewSet

from .models import Worker, SalesPoint, Visiting
from .serializers import WorkerSerializer, SalesPointSerializer, VisitingSerializer


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class SalesPointViewSet(ModelViewSet):
    queryset = SalesPoint.objects.all()
    serializer_class = WorkerSerializer


class VisitingViewSet(ModelViewSet):
    queryset = Visiting.objects.all()
    serializer_class = WorkerSerializer
