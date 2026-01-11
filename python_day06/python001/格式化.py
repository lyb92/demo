# name = input("姓名：")
# phone = input("手机号：")
# print("姓名--%s；手机号--%s" %(name,phone))


name_1 = input("姓名：")
score_1 = input("成绩：")
name_2 = input("姓名：")
score_2 = input("成绩：")
avg_score = (int(score_1)+int(score_2))/2
print("姓名\t成绩")   #\t,横向制表符（相当于按一次tab） 
print("%s\t%s\n%s\t%s\n平均成绩\t%.2f" %(name_1,score_1,name_2,score_2,avg_score))