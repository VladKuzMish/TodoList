from rest_framework import viewsets

from todo_structure.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Вьюсет модели Todo."""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
