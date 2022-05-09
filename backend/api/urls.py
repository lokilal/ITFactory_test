from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SalesPointViewSet, WorkerFilterViewSet

v1_router = DefaultRouter()
v1_router.register('sales_point', SalesPointViewSet)
v1_router.register('worker', WorkerFilterViewSet, basename='worker')

urlpatterns = [
    path('v1/', include(v1_router.urls))
]
