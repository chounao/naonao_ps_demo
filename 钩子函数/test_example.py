# test_example.py
import pytest

@pytest.mark.run(order=1)
def test_first():
    print("**************001*******************")
    assert True

@pytest.mark.run(order=2)
def test_second():
    print("**************002*******************")

    assert True

if __name__ == '__main__':
    pytest.main(['-vs'])