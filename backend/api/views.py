from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import SalesPoint, Worker
from .serializers import SalesPointSerializer, WorkerSerializer
from .filters import WorkerFilter


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkerFilter


class SalesPointViewSet(ModelViewSet):
    queryset = SalesPoint.objects.all()
    serializer_class = SalesPointSerializer

    def get(self):
        print("yes")
