s = "abcd abdd abff adff"
print(s.count("ab"))                # 返回整个字符串中"ab"的数量
print(s.count("ab",5))              # 返回整个字符串第6个位置开始的所有"ab"的数量
print(s.count("ab",5,9))            # 返回整个字符串第6个位置到第十个位置的所有"ab"的数量
print(s.count("ab",5,-1))           # 返回整个字符串第6个位置到最后一个位置的所有"ab"的数量