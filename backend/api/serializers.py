from rest_framework import serializers

from .models import Worker, SalesPoint, Visiting


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class SalesPointSerializer(serializers.ModelSerializer):
    worker = serializers.PrimaryKeyRelatedField(

    )

    class Meta:
        model = SalesPoint
        fields = '__all__'


class VisitingSerializer(serializers.ModelSerializer):
    sales_point = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Visiting
        fields = '__all__'
