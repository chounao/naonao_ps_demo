import pytest
@pytest.fixture
def a():

    A =+1
    print(A,"+++++++++++++++")
    yield A

def test_a(a):
    b = a+1
    print(b,"=============")
