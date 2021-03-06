import pytest


@pytest.fixture
def assignee(factory):
    return factory.user()


@pytest.fixture
def todo(factory, assignee):
    defaults = {
        'text': 'The Todo',
        'assignee': assignee,
    }
    return factory.todo(**defaults)
