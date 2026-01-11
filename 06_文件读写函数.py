"""一次读取一行"""

f = open("a.txt", "r")
# content1 = f.readline()
# content2 = f.readline()
# content3 = f.readline()
# print(content1)
# print(content2)
# print(content3)
# f.close()

lines = f.readline()
print(lines)
for line in lines:
    if line[-1] == "\n":
        print(line[:-1])
    else:
        print(line)
f.close()
