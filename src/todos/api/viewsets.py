from rest_framework.decorators import action

from app.api.viewsets import DefaultModelViewSet
from todos.api import serializers
from todos.models import Todo


class TodoViewSet(DefaultModelViewSet):
    serializer_class = serializers.TodoSerializer
    serializer_action_classes = {
        'create': serializers.TodoCreateSerializer,
        'update': serializers.TodoUpdateSerializer,
        'partial_update': serializers.TodoUpdateSerializer,
    }
    queryset = Todo.objects.all()

    @action(detail=True, methods=['POST'])
    def open(self, request, pk=None):
        todo = self.get_object()
        todo.status = 'opened'  # No service
        todo.save()
        return self.response(todo, 201)

    @action(detail=True, methods=['POST'])
    def close(self, request, pk=None):
        todo = self.get_object()
        todo.status = 'closed'  # No service
        todo.save()
        return self.response(todo, 201)
