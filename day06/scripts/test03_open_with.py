""""
    目标：open 与 with open区别
        1.共同点：打开文件
        2.不同点：with open = 执行打开操作 + 关闭操作
"""
try:
    f = open("../report/text.txt", "r", encoding="utf_8")
    print(f.read())
except:
    pass
finally:
    f.close()

"""
with open 极力推荐
"""


with open("../report/text.txt","r",encoding="utf_8") as f:
  f.read()
