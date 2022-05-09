from django.db import models


class Worker(models.Model):
    name = models.CharField(
        max_length=255, verbose_name='Имя'
    )
    phone_number = models.CharField(
        max_length=255, verbose_name='Номер телефона',
        unique=True
    )

    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class SalesPoint(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название'
    )
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, verbose_name='Работник',
        related_name='sales_point'
    )

    def __str__(self):
        return self.title


class Visiting(models.Model):
    date = models.DateTimeField(
        verbose_name='Дата/время'
    )
    sales_point = models.ForeignKey(
        SalesPoint, on_delete=models.CASCADE, verbose_name='Торговая точка'
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )
