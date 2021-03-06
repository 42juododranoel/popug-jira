import pytest

pytestmark = [pytest.mark.django_db]


def test_close_todo(as_user, todo, assignee):
    got = as_user.post(f'/api/v1/todos/{todo.id}/close/')

    assert got['status'] == 'closed'
