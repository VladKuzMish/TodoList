import uuid

from django.db import models


class Todo(models.Model):
    """Модель приложения Todo."""

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=8
        )
    created = models.DateTimeField(
        'Дата создания', auto_now_add=True
    )
    body = models.CharField(max_length=2000)
    active = models.SlugField(unique=True)
