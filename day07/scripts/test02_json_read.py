"""
     目标：写入json
     案例：
         读取data/write.json
     操作：
         1.导包json
         2.方法load(文件流)
     注意：
         1.写入操作 W
         2.写入方法：dump()而不是dumps()
"""
# 导包
import json


# 打开要调用的文件流，并调用load方法
with open("../data/write.json", "r", encoding="utf_8") as f:
    data = json.load(f)
    print(data)
