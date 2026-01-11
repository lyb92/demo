# 导包
import json


def read_json(filename):
    full_path = "\\PycharmProjects123\\day06_2\\V4_2\\data\\" + filename
    # 调用load方法
    with open(full_path, "r", encoding="utf_8") as f:
        return json.load(f)


if __name__ == "__main__":
    datas = read_json("calc.json")
    print(datas)
    print("-----------------------")
    """
    # 期望的格式：[(1,2,3),(1001,2,1003)]
    # 问题：
    #     1.返回的格式为字典
    # 新建空列表
    """
    # 新建空列表
    arrs = []
    for data in datas.values():
        arrs.append((data['a'], data['b'], data['expect']))
    print(arrs)
