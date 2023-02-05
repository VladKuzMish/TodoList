import uuid

from django.db import models

from .constants import TEXT_LIMIT


class UUIDBaseModel(models.Model):
    """Базовая модель для генерации UUID."""

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    class Meta:
        abstract = True

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None, 
        update_fields=None
    ):
        self._set_unique_uuid()
        super().save(force_insert, force_update, using, update_fields)

    def _set_unique_uuid(self):
        if self._meta.model.objects.filter(uuid=self.uuid).exists():
            self.uuid = uuid.uuid4()
            self._set_unique_uuid()


class Todo(UUIDBaseModel):
    """Модель приложения Todo."""

    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    body = models.TextField(
        'Описание',
        max_length=2000,
    )
    active = models.BooleanField(
        'Статус',
        default=True,
    )

    def __str__(self):
        return self.body[:TEXT_LIMIT]
