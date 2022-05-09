from django.contrib import admin

from .models import SalesPoint, Worker, Visiting


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone_number', )
    search_fields = ('name', )


class SalesPointAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    search_fields = ('title', )


class VisitingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'sales_point', 'latitude', 'longitude', )
    search_fields = ('sales_point__title', 'sales_point__worker__name', )


admin.site.register(Worker, WorkerAdmin)
admin.site.register(SalesPoint, SalesPointAdmin)
admin.site.register(Visiting, VisitingAdmin)
