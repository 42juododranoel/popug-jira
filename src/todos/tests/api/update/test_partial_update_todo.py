import pytest

pytestmark = [pytest.mark.django_db]


def test_partial_update_todo_instance(as_user, todo, new_assignee):
    as_user.patch(f'/api/v1/todos/{todo.id}/', {
        'text': 'The New Todo',
        'assignee': new_assignee.id,
    })

    todo.refresh_from_db()
    assert todo.text == 'The New Todo'
    assert todo.assignee == new_assignee


def test_partial_update_todo_response(as_user, todo, new_assignee):
    got = as_user.patch(f'/api/v1/todos/{todo.id}/', {
        'text': 'The New Todo',
        'assignee': new_assignee.id,
    })

    assert got['text'] == 'The New Todo'
    assert got['assignee']['id'] == new_assignee.id
