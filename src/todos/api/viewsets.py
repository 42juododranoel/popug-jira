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
