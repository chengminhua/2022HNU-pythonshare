# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月20日
"""
# 第一关
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 06:29:54 2020

@author: hzh
"""

# 第1题：
year = eval(input())
####### begin #######
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("yes")

####### end #########
# 如果不是闰年，输出no
####### begin #######
else:
    print("no")
####### end #########

# 第2题:
month_list = [1, 3, 5, 7, 8, 10, 12]  # 31天
small_month_list = [4, 6, 9, 11]  # 30天
month = int(input())
# 31天的月份：1~7之间的奇数月、8~12之间的偶数月
# 如果是31天的月份输出yes
####### begin #######
if month in small_month_list:
    print("yes")
else:
    print("no")
####### end #########
# 如果不是30天的月份，输出no
####### begin #######

####### end #########


# 第3题:
# 从键盘输入成绩，等级默认为0级
scores = int(input())
grade = '0'
# 如果成绩>=90分的输出'A'
####### begin #######
if scores >= 90:
    print("A")
####### end #########
# 否则成绩60-89分之间的用B表示
elif 60 <= scores <= 89:
    print("B")
####### end #########
# 60分以下的用C表示
else:
    print("C")
####### end #########


# 第4题:
# 从测试集得到风速
velocity = int(input())
# 默认是0级
rank = 0
# 如果风速在74到95之间，输出1
####### begin #######
if 74 <= velocity <= 95:
    rank = 1
####### end #########
# 如果风速在96到110之间，输出2
####### begin #######
if 96 <= velocity <= 110:
    rank = 2
####### end #########
# 如果风速在111到130之间，输出3
####### begin #######
if 111 <= velocity <= 130:
    rank = 3
####### end #########
# 如果风速在131到154之间，输出4
####### begin #######
if 131 <= velocity <= 154:
    rank = 4
####### end #########
# 如果风速大于155，输出5
####### begin #######
if velocity >= 155:
    rank = 5
####### end #########
print(rank)


# 第二关
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 07:49:34 2020

@author: hzh
"""


# 第一题
def sortThree(num1, num2, num3):
    # 函数说明
    # 参数为待排序的3个数
    # 返回排序后的3个数
    # 请在下面编写代码
    # ********** Begin ********** #
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2

    # ********** End ********** #
    # 请不要修改下面的代码
    return num1, num2, num3


n1, n2, n3 = eval(input())
sx1, sx2, sx3 = sortThree(n1, n2, n3)
if type(sx1) == float or type(sx2) == float or type(sx3) == float:
    print("%.4f,%.4f,%.4f" % (sx1, sx2, sx3))
else:
    print(sx1, sx2, sx3, sep=',')
# print('\n***********************\n')

# 第二题
import math


def solve(a, b, c):
    # 函数说明
    # 参数a,b,c分别代表方程的三个系数
    # 返回方程的两个根
    # 请在下面编写代码
    # ********** Begin ********** #
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        root1, root2 = "None", "None"
    else:
        root1 = (-b + delta ** 0.5) / (2 * a)
        root2 = (-b - delta ** 0.5) / (2 * a)
    # ********** End ********** #
    # 请不要修改下面的代码
    return root1, root2


a, b, c = eval(input())
r1, r2 = solve(a, b, c)
if type(r1) == float or type(r2) == float:
    print("%.4f,%.4f" % (r1, r2))
else:
    print(r1, r2)


# print('\n***********************\n')

# 第三题
# for x in [-9, -8, -7, -6, -5, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]:
def calexpress(x):
    # 请在下面编写代码
    # ********** Begin ********** #
    if -10 <= x < -8:
        fx = x - 2
    elif -8 <= x < -6:
        fx = x + 3
    elif -6 <= x <= -2:
        fx = x ** 2
    elif -2 < x < 2:
        fx = abs(x)
    elif 2 <= x <= 4:
        fx = x ** 3
    elif 4 < x <= 6:
        fx = 3 * x - 4
    elif 6 < x <= 8:
        fx = 4 * x + 1
    else:
        fx = "None"
    # ********** End ********** #
    # 请不要修改下面的代码
    return fx


x = eval(input())
fx = calexpress(x)
if type(fx) == float:
    print("%.4f" % fx)
else:
    print(fx)

# 第三关
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:27:35 2020

@author: hzh
"""


# 第一题
def BMI(w, h):
    # 函数说明
    # 参数h表示体重，h表示身高
    # 函数返回BMI值wto(国际), dom(国内)
    wto, dom = '', ''
    # 请在下面编写代码
    # wto, dom的结果为字符串类型的"肥胖"，"偏瘦"，"偏胖"，"正常"
    # ********** Begin ********** #
    bmi = w / pow(h, 2)
    if bmi < 18.5:
        wto = "偏瘦"
    elif 18.5 <= bmi < 25:
        wto = "正常"
    elif 25 <= bmi < 30:
        wto = "偏胖"
    else:
        wto = "肥胖"

    if bmi < 18.5:
        dom = "偏瘦"
    elif 18.5 <= bmi < 24:
        dom = "正常"
    elif 24 <= bmi < 28:
        dom = "偏胖"
    else:
        dom = "肥胖"
    # ********** End ********** #
    return wto, dom
    # 请不要修改下面的代码


Weight, Height = eval(input())
wto, dom = BMI(Weight, Height)
print("BMI 指标为:国际'{0}', 国内'{1}'".format(wto, dom))


# print('\n******************************\n')

# 第二题
def calSalaTax(salary):
    # 函数说明
    # 参数salary表示工作数
    # 返回所得税费Tax
    Tax = 0
    # 请在下面编写代码
    # ********** Begin ********** #
    if salary <= 0:
        Tax = 0
    elif salary <= 47449:
        Tax = salary * 0.22
    elif salary <= 114649:
        Tax = salary * 0.25
    elif salary <= 174699:
        Tax = salary * 0.28
    elif salary <= 311949:
        Tax = salary * 0.33
    else:
        Tax = salary * 0.35

    # ********** End ********** #
    # 请不要修改下面的代码
    return Tax


salary = eval(input())
salaTax = calSalaTax(salary)
print("%.4f" % salaTax)


# print('\n***********************\n')

# 第三题
# for (p1, p2) in [('s', 'j'), ('b', 'j'),('j', 'j'), ('b', 's')]:
def boxgGame(p1, p2):
    # 函数说明
    # 参数：p1,p2代表玩家1，玩家2，其值为's','j','b' 分别代表石头剪刀和布
    # 返回值：game=-1，0，1分别代表p1输局，平局，赢局
    # ********** Begin ********** #
    if p1 == p2:
        game = 0
    elif p1 == "s" and p2 == "j":
        game = 1
    elif p1 == "j" and p2 == "b":
        game = 1
    elif p1 == "b" and p2 == "s":
        game = 1
    else:
        game = -1
    # ********** End ********** #
    # 请不要修改下面的代码
    return game


p1, p2 = input().split(',')
game = boxgGame(p1, p2)
print(game)
# print('\n***********************\n')
