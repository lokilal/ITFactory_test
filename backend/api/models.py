from django.db import models


class Worker(models.Model):
    name = models.CharField(
        max_length=255, verbose_name='Имя'
    )
    phone_number = models.CharField(
        max_length=255, verbose_name='Номер телефона',
        unique=True
    )

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class SalesPoint(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название'
    )
    worker = models.ManyToManyField(
        Worker, verbose_name='Работник',
        related_name='sales_point'
    )

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

    def __str__(self):
        return self.title


class Visiting(models.Model):
    date = models.DateTimeField(
        verbose_name='Дата/время', auto_now_add=True
    )
    sales_point = models.ForeignKey(
        SalesPoint, on_delete=models.CASCADE, verbose_name='Торговая точка',
        related_name='visiting'
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещение'

    def __str__(self):
        return f'{self.latitude:.5f} - {self.longitude:.5f}'
