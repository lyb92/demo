def fun(*parm):
    print(type(parm))
    for item in parm:
        print(item)


fun("haha")
fun(*(10, 20, 30, 40), *(22, 55, 99, 33))
fun(*[11, 22, 33, 44, 55])
fun(*{"name": "李四", "age": 19, "height": 176})


def fun2(**par):
    print(type(par))
    for key, value in par.items():
        print(key, "--------", value)


fun2(name="张三", age=18, height=178)

d1 = {"name": "李四", "age": 19, "height": 176}
d2 = {"name": "王五", "age": 17, "height": 175}
fun2(**d1)
fun2(**d2)


def get_sum(num):
    s = 0
    odd_sum = 0
    even_sum = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            odd_sum += i
        else:
            even_sum += i
        s += i
    return s, odd_sum, even_sum


result = get_sum(10)
print(type(result))
print(result)

a, b, c = get_sum(10)

print(a, b, c)
