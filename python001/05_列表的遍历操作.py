# break continue 用在循环中，问题：能否在for循环使用break 和 continue.

# 嵌套的列表遍
my_list = [[10, 20, 30], [100, 200, 300], [1000, 2000, 3000]]

i = 0
while i < len(my_list):
    # my_list[i]是什么类型？
    j = 0
while j < len(my_list[i]):
    print(my_list[i][j])
    j += 1
i += 1

print("*" * 30)

for o in my_list:
    for v in o:
        print(v)
