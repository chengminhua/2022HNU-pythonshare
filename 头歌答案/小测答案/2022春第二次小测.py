# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月17日
"""

# 第一题
year = eval(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("闰年")
else :
    print("平年")

# 第二题
age = eval(input("please input your age:"))
label = ""
if age < 18 :
    label = "underage"
elif 18 <= age < 40:
    label = "young man"
elif 40 <= age < 60 :
    label = "middle-aged"
else:
    label = "old man"

print("You are {}.".format(label))

# 第三题
height,weight = eval(input())
height = height * 0.01
BMI = weight / (height ** 2)

global_ = ""
home = ""
if BMI < 18.5 :
    global_ = "偏瘦"
elif 18.5 <= BMI < 25:
    global_ = "正常"
elif 25 <= BMI < 30:
    global_ = "偏胖"
else :
    global_ = "肥胖"

if BMI < 18.5 :
    home = "偏瘦"
elif 18.5 <= BMI < 24:
    home = "正常"
elif 24 <= BMI < 28:
    home = "偏胖"
else :
    home = "肥胖"

print("国际{},国内{}".format(global_,home))

# 第四题
num1,num2 = eval(input())
fuhao = input()

if num2 == 0:
    print("除数不能为0")
elif fuhao == "+":
    print(num1 + num2)
elif fuhao == "-":
    print(num1 - num2)
elif fuhao == "*":
    print(num1 * num2)
elif fuhao == "/":
    print(num1 / num2)
elif fuhao == "//":
    print(num1 // num2)
elif fuhao == "%":
    print(num1 % num2)
elif fuhao == "**":
    print(num1 ** num2)