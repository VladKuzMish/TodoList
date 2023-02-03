import uuid

from django.db import models

from .constants import TEXT_LIMIT


class Todo(models.Model):
    """Модель приложения Todo."""

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    created = models.DateTimeField(
        'Дата создания', auto_now_add=True
    )
    body = models.CharField(max_length=2000)
    active = models.SlugField(unique=True)

    def __str__(self):
        return self.uuid[:TEXT_LIMIT] 
