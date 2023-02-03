from rest_framework import serializers

from todo_structure.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки объектов модели Todo."""

    class Meta:
        model = Todo
        fields = (
            "id",
            "uuid",
            "created",
            "body",
            "active",
        )
