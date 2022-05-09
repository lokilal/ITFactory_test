import django_filters as filters

from .models import Worker


class WorkerFilter(filters.FilterSet):
    class Meta:
        model = Worker
        fields = ('phone_number', )
