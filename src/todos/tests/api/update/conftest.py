import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def new_assignee(factory):
    return factory.user()
