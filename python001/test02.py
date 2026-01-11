list_of_lists = [['123.45,456.78'],['13.45,56.78']]
list2 = ['123.45,456.78','13.45,56.78']
# list1 = [[int(item) for item in sublist] for sublist int list1]
list_of_lists = [[int(item) if item.isdigit() else item for item in sublist] for sublist in list_of_lists]

# list_of_lists = [[int(item) for item in sublist] for sublist in list_of_lists]
# int(list2)
# print(type(list2))
# print(list_of_lists)
# 使用嵌套for循环遍历二维列表
# x=[]
for row in list_of_lists:
    for item in row:
        # print(row)
        # int(item)
        list_from_string = item.split(',')
        # print(list_from_string)
        x = list(map(float, list_from_string))
        print(x)

    # x = list(map(int, item))
    # print(x)