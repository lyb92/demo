poetry = "远看泰山黑乎乎，上头细来下头粗。茹把泰山倒过来，下头细来上头粗，茹"

# replace 并不会替换原本的字符串，替换完毕之后返回一个新的字符串
new_poetry = poetry.replace("茹", "如")
print(poetry)
print(new_poetry)
new_poetry=poetry.replace("茹", "如",1)
print(new_poetry)