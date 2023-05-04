import pytest
@pytest.fixture()
def setup():
    print("hello")
    print("hi")
    yield
    print("nice")
    print("bye")


def test_setup1():
    print("hi how are you")

def test_setup2():
    print("hi i am fine")
