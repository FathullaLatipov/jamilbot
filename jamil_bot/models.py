from django.db import models


class VehicleModel(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'vehicle'
        verbose_name_plural = 'vehicles'


class UsernameModel(models.Model):
    tg_username = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=13)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'
