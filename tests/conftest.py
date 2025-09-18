import pytest


@pytest.fixture(scope='session', autouse=True)
def run_db():
    print('\nSTART DB')

    yield

    print('\nSTOP DB')
