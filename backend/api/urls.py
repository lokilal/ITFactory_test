from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SalesPointViewSet, WorkerViewSet

v1_router = DefaultRouter()
v1_router.register('sales_point', SalesPointViewSet)
v1_router.register('worker', WorkerViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls))
]
