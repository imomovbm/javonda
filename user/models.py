
from django.db import models
from django.contrib.auth.models import User


class FoydalanuvchiProfili(models.Model):

    ROLLAR = [
        ('user', 'Foydalanuvchi'),
        ('admin', 'Admin'),
        ('courier', 'Kuryer'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Foydalanuvchi"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLLAR,
        default='user',
        verbose_name="Rol"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Telefon raqami"
    )

    def __str__(self):
        return self.user.username
