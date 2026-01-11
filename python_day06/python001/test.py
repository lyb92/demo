def get_data(txt_path: str = '', epoch: int = 100, target: str = '', target_data_len: int = 100):
    num_list = []  # 将提取出来的数据保存到列表,并在最后返回
    data = open(txt_path, encoding="utf-8")  # 打开文件
    str1 = data.read()  # 将文件中读取到的内容转化为字符串
    data.close()  # 关闭文件
    for i in range(0, epoch):
        index = str1.find(target)  # 查找字符串str1中str2字符串的位置

        num_list.append(float(str1[index+len(target):index+len(target)+target_data_len]))  # 将需要的数据提取到列表中
        # num_list.append(target_data_len)  # 将需要的数据提取到列表中
        str1 = str1.replace(target, 'xxxx', 1)  # 替换掉已经查阅过的地方,' xxxx '表示替换后的内容，1表示在字符串中的替换次数为1
    return num_list
data_path = "D:/program/test/1.txt"
# 提取x1的数据
list_x1  = get_data(data_path, 6, target="x1:", target_data_len=7)
# 提取test3的数据
list_test3  = get_data(data_path, 6, target="test3:", target_data_len=6)
# 提取y4的数据
list_y4  = get_data(data_path, 6, target="y4:", target_data_len=8)
print(list_x1)
print(list_test3)
print(list_y4)