from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements',
        verbose_name='Датчик'
    )
    temperature = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name='Температура'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время измерения'
    )
    # Дополнительное задание: поле для картинки
    image = models.ImageField(
        upload_to='measurements/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Измерение температуры'
        verbose_name_plural = 'Измерения температуры'

    def __str__(self):
        return f'{self.sensor.name} - {self.temperature}°C'
