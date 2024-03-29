from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='img/')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.descripcion