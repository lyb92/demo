import random

num = random.randint(1, 100)
count = 0
flag = True
while flag:
    guess_num = int(input("请输入猜测的数字"))
    count += 1
    if guess_num == num:
        print("恭喜你，猜对了")
        flag = False
    elif guess_num > num:
        print("猜大了")
    else:
        print("猜小了")
print(f"你一共猜了{count}次")
