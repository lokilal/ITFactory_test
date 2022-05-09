from rest_framework import serializers

from .models import Worker, SalesPoint


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'


class SalesPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesPoint
        fields = ('id', 'title', )

"""
    def to_representation(self, instance):
        data = super(SalesPointSerializer, self).to_representation(instance)
        obj = Worker.objects.get(pk=data['worker'])
        data['worker'] = WorkerSerializer(obj).data
        return data
"""