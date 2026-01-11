import random
#获得用户输入的拳头
user_quan =int(input("请出拳 石头(0)、箭刀(1)、布(2):"))
#获得电脑的拳头randint 用于产生一个范围的随机数
computer_quan = random.randint(0,2)

#判断胜负
#玩家胜利的情况

if(user_quan == 0 and computer_quan ==1) or\
        (user_quan==1 and computer_quan ==2)or\
        (user_quan==2 and computer_quan ==0):
     print("您赢了")
elif user_quan == computer_quan:
    print("平局！")
else:
    print("您输了！")
