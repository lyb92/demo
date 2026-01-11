def cacl2(a, b):
    s = a + b
    return s


get_sum = cacl2(2, 3)
print(get_sum)

get_sum2 = cacl2(cacl2(2, 3), 20)
print(get_sum2)


def get_sum(num):
    sum = 0
    odd_sum = 0
    even_sum = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            odd_sum += i
        else:
            even_sum += i
        sum = odd_sum + even_sum
    return odd_sum, even_sum, sum


result = get_sum(100)
print(type(result))
print(result)

a, b, c = get_sum(100)
print(a)
print(b)
print(c)
