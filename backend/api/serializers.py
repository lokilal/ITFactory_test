from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import SalesPoint, Visiting


class SalesPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesPoint
        fields = ('id', 'title', )


class VisitingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visiting
        fields = '__all__'

    def to_representation(self, instance):
        data = {
            'id': instance.pk,
            'date': instance.date
        }
        return data

    def validate(self, attrs):
        phone_number = self.context['phone_number']
        sale_point = get_object_or_404(SalesPoint, pk=attrs['sales_point'].pk)
        if sale_point.worker.phone_number != phone_number:
            raise serializers.ValidationError(
             'Переданный номер не привязан к торговой точке'
            )
        return attrs
