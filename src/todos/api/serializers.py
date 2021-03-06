from rest_framework import serializers

from users.api.serializers import UserSerializer
from todos.models import Todo


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'text',
            'assignee',
        ]


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'text',
            'assignee',
        ]


class TodoSerializer(serializers.ModelSerializer):
    assignee = UserSerializer()

    class Meta:
        model = Todo
        fields = [
            'id',
            'text',
            'assignee',
        ]
