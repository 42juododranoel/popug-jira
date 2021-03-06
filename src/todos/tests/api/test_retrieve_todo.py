import pytest

pytestmark = [pytest.mark.django_db]


def test_retrieve_todo(as_anon, todo, assignee):
    got = as_anon.get(f'/api/v1/todos/{todo.id}/')

    assert got['text'] == 'The Todo'
    assert got['status'] == 'opened'
    assert got['assignee']['id'] == assignee.id
