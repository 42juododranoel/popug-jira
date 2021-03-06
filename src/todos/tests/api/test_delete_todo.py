import pytest

pytestmark = [pytest.mark.django_db]


def test_delete_todo_instance(as_user, todo):
    as_user.delete(f'/api/v1/todos/{todo.id}/')

    with pytest.raises(todo.DoesNotExist):
        todo.refresh_from_db()
