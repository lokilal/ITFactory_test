from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SalesPointViewSet

v1_router = DefaultRouter()
v1_router.register('sales_point', SalesPointViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls))
]
