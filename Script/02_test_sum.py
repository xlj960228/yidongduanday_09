import pytest
import yaml,os

from Base.getData import GetData


def get_sum_data():
    #定义存储数据列表
    sum_list = []
    #读n os.scp:获取系统路径分隔符 因为unix分隔符为: "/"  window ""\
    # with open("./data" + os.sep + "sum.yml", "r", encoding="utf-8") as f:
    #     #解析
    #     data = yaml.safe_load(f)
    data = GetData().get_yml_data("sum.yml")

    for i in data.values():
        sum_list.append(tuple(i.values()))
    print(sum_list)

    return sum_list


class TestSum:
    @pytest.mark.parametrize("a,b,c",get_sum_data())
    def test_sum(self,a, b, c):
        print("{}+{}={}".format(a, b, c))
        assert a + b == c