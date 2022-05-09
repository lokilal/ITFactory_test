from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Worker, Visiting
from .serializers import SalesPointSerializer, VisitingSerializer


class WorkerFilterViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        phone_number = request.GET.get('phone_number')
        if not phone_number:
            return Response({
                'Не указан номер телефона': status.HTTP_400_BAD_REQUEST
            })
        worker = get_object_or_404(Worker, phone_number=phone_number)
        sales_point = worker.sales_point.all()
        return Response(SalesPointSerializer(sales_point, many=True).data)


class VisitingViewSet(ModelViewSet):
    queryset = Visiting.objects.all()
    serializer_class = VisitingSerializer

    def create(self, request, *args, **kwargs):
        phone_number = request.GET.get('phone_number')
        if not phone_number:
            return Response({
                'Не указан номер телефона': status.HTTP_400_BAD_REQUEST
            })
        data = {'phone_number': phone_number}
        serializer = self.serializer_class(
            data=request.data,
            context=data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
