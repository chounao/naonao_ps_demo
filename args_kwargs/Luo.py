

# @pytest.fixture()
# def setup_and_teardown():
#     yield
#     print("Running test_02")
#
# def test_01(setup_and_teardown):
#     a = 1
#     b = 3
#     assert a + b == 4
#
# def test_02(setup_and_teardown):
#     c = 3
#     assert c * 2 == 6


# # 定义一个 fixture，用于提供测试数据
# @pytest.fixture()
# def input_data():
#     data = [1, 2, 3, 4, 5]
#     print("Initializing input data")
#     yield data
#     print("Cleaning up input data")
#
# # 使用 input_data fixture 进行测试
# def test_data_length(input_data):
#     assert len(input_data) == 5
#
# # 使用 input_data fixture 进行另一个测试
# def test_data_sum(input_data):
#     assert sum(input_data) == 15
# import pytest
# @pytest.fixture(scope="function", params=["1", "2"])
# def autotest(request):
#     return request.param
#
#
# class TestApi:
#     def test_case_1(self, autotest):
#         print(autotest)
#         print(" test_case_1")
#
#     def test_case_2(self):
#         print(" test_case_2")

import pytest

@pytest.fixture
def setup_and_teardown():
    h = 5
    print(2*h)
    yield
    print("**********************")

@pytest.mark.parametrize('a', [1, 2])
def test_01(a,setup_and_teardown):
    b = 3
    print("0001================")
    assert a + b == 4

def test_02():
    c = 3
    print("002================")
    assert c * 2 == 6



if __name__ == '__main__':
    pytest.main(['-s'])