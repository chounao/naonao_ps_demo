import pytest
@pytest.fixture(scope='class',params=['1','2'])
def data(request):
    return request.param

class Test_data:
    def test_01(self,data):
        print("查询")
        print(data)

    def test_02(self,data):
        print("下单")
        print(data)

    def test_03(self, data):
        print("取消")
        print(data)
