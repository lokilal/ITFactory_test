from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import SalesPoint, Worker
from .serializers import SalesPointSerializer, WorkerSerializer


class WorkerFilterViewSet(ViewSet):

    def list(self, request):
        phone_number = request.GET.get('phone_number')
        if not phone_number:
            return Response({
                'Не указан номер телефона': status.HTTP_400_BAD_REQUEST
            })
        worker = get_object_or_404(Worker, phone_number=phone_number)
        sales_point = worker.sales_point.all()
        return Response(SalesPointSerializer(sales_point, many=True).data)


class SalesPointViewSet(ViewSet):
    queryset = SalesPoint.objects.all()
    serializer_class = SalesPointSerializer
