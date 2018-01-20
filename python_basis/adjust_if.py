# 条件判断
age = 30
if (age > 10 and age < 15):
    print("少年")
elif (age >= 15 and age < 25):
    print("中年")
else:
    print("老年了逗比")

# 条件判断与input进行集成
birth = input("birth: ")
birthInt = int(birth)
if (birthInt == 1993):
    print("咱俩是同一年生的")
else:
    print("咱俩不是同一年生的")
