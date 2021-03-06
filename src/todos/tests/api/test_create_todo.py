import pytest

from todos.models import Todo

pytestmark = [pytest.mark.django_db]


def test_create_todo_instance(as_user, assignee):
    as_user.post('/api/v1/todos/', {
        'text': 'The Todo',
        'assignee': assignee.id,
    })

    todo = Todo.objects.last()
    assert todo.text == 'The Todo'
    assert todo.assignee == assignee


def test_create_todo_response(as_user, assignee):
    got = as_user.post('/api/v1/todos/', {
        'text': 'The Todo',
        'assignee': assignee.id,
    })

    assert got['text'] == 'The Todo'
    assert got['assignee']['id'] == assignee.id
