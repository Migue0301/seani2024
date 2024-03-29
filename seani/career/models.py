from django.db import models

# Create your models here.
class Career(models.Model):

    LEVELS = [
        ('TSU', 'Técnico Superior Universitario'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestría')
    ]
    name = models.CharField(
        verbose_name ='Nombre',
        max_length = 200,
    )
    short_name = models.CharField(
        verbose_name ='Abreviarura',
        max_length = 10,
    )
    level = models.CharField(
        verbose_name='Nivel',
        max_length=10,
        choices = LEVELS,
    )

    def _srt_(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'carrera',
        verbose_name_plural = 'carreras'