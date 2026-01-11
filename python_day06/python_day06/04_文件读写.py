# 使用open 函数打开一个文件
fa = open("a.txt", "w")
my_content = "hello world! 第一次写入文件！\n"
fa.write(my_content)
# 关闭文件
fa.close()

# 2. 读取文件数据
fb = open("b.txt", "r",encoding="UTF-8")
# read 函数默认读取文件中的所有数据
my_content = fb.read()
print(my_content)
fb.close()

# print(my_content)

def test03():

    f = open("a.txt","a")
    f.write("\n hello python")
    f.close()

test03()





