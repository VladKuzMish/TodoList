from rest_framework import generics
from rest_framework import permissions

from todo_structure.models import Todo
from .serializers import TodoSerializer


class TodoCreate(generics.ListCreateAPIView):
    """ Дженерик создания и получения записей."""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TodoDelete(generics.RetrieveUpdateDestroyAPIView):
    """ Дженерик удаления и изменения записей."""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAdminUser,)
