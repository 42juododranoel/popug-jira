import pytest

pytestmark = [pytest.mark.django_db]


def test_open_todo(as_user, todo, assignee):
    got = as_user.post(f'/api/v1/todos/{todo.id}/open/')

    assert got['status'] == 'opened'
