from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username if self.username else None


class UserInfoDevices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='device_info')
    device = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    browser_version = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50)
    is_bot = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.device} - {self.browser}"
