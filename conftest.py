import pytest


@pytest.fixture
def numbers():
    numList = [i for i in range(1, 101) if i % 2 == 0]
    return numList

@pytest.fixture(autouse=True)
def hello_world():
    print("hello world")