import pytest

pytestmark = [pytest.mark.django_db]


def test_list_todos(as_anon, todo, assignee):
    got = as_anon.get('/api/v1/todos/')

    assert got['results'][0]['text'] == 'The Todo'
    assert got['results'][0]['assignee']['id'] == assignee.id
