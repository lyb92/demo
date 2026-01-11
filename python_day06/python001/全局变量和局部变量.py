# 定义全局变量  全局作用域
my_number = 100


# 就近原则
# 定义要先定义再使用
# 作用域：表示变量能够使用的范围
def my_function():
    my_number = 20
    print(my_number)
 # my_number = 20

my_function()
print(my_number)
