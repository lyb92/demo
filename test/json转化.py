import json

data = {"name": "张三", "age": 18}
print("转换之前：", type(data))
d1 = json.dumps(data)
print("转换之后：", type(d1))
print(d1)

data = '{"name": "张三", "age": 18}'
print("转换之前：", type(data))
d2 = json.loads(data)
print("转换之后：", type(d2))
print(d2)
