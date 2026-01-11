score = float(input("请输入分数:"))
# if score > 90 and score < 100:
#     print("太棒了")
# elif score > 80 and score <= 90:
#     print("优秀")
# elif score > 70 and score <= 80:
#     print("良好")
# elif score > 60 and score <= 70:
#     print("合格")
# elif score >100 or score < 0:
#     print("输入错误")
# else:
#     print("你完了")

if score>=0 and score<=100:
    if score > 90 and score < 100:
        print("太棒了")
    elif score > 80 and score <= 90:
        print("优秀")
    elif score > 70 and score <= 80:
        print("良好")
    elif score > 60 and score <= 70:
        print("合格")
    else:
        print("你完了")
else:
    print("输入错误")