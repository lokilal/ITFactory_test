from django.contrib import admin

from .models import SalesPoint, Worker, Visiting

admin.site.register(SalesPoint)
admin.site.register(Worker)
admin.site.register(Visiting)
