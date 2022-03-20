# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月20日
"""
# 第一关
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:54:44 2020

@author: hzh
"""
from math import *

i = 1  # 当前计算的值
s = 0  # 计算出来的和
# 第1题
########### begin ##########
for i in range(1, 1000, 2):
    s += i ** 2

######### end     ####
print(s)

########## 第2题 ##############
x = int(input())

if x < 0:
    print('无实数解')
else:
    g = x / 2
    #######begin##############
    # 请输入while循环控制语句
    eps = 10e-6
    while not abs(x - g * g) < eps:
        g = (g + x / g) / 2

    #######end#################
    print("%.4f" % g)

########## 第3题 ##############
# 计算并输出三位数内的水仙花数
####### Begin #########
# 请在此输入for循环表达式
for i in range(100, 1000):
    x1 = i // 100
    x2 = i % 100 // 10
    x3 = i % 10
    if x1 ** 3 + x2 ** 3 + x3 ** 3 == i:
        print(i)

####### End ########


# 第二关
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:18:27 2021

@author: hzh
"""
# 第一题:从键盘输入m行n列，在屏幕上输出m行n列的*行图案
m, n = eval(input())
# 请在下面编写代码
# ********** Begin ********** #
for i in range(m):
    print("*" * n)

# ********** End ********** #

# 第二题:从键盘输入m行,在屏幕上输出m行的直角图案
m = eval(input())
# 请在下面编写代码
# ********** Begin ********** #
for i in range(1, m + 1):
    print("*" * (2 * i - 1))

# ********** End ********** #

# 第三题:从键盘输入m行,在屏幕上输出m行的等腰三角形图案
m = eval(input())
# 请在下面编写代码
# ********** Begin ********** #
for i in range(1, m + 1):
    print(" " * (m - i) + "*" * (2 * i - 1))

# ********** End ********** #


# 第三关
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:49:56 2020

@author: hzh
"""
from math import *

# 任务一：三天打鱼两天晒网
dayup, dayfactor = 1.0, 0.01
# 请在下面编写代码
# ********** begin ********** #
dayup = (dayup - dayfactor) ** 146 * (dayup + dayfactor) ** 219

# ********** End ********** #
# 请不要修改下面的代码
print("{:.2f}.".format(dayup))

# 任务二：天天向上的力量
import math

dayup, dayfactor = 1.0, 0.01
ddup = math.pow((dayup + dayfactor), 365)


# print("天天向上的力量: {:.2f}.".format(ddup)) 37.78
# 请在下面编写代码
# ********** Begin ********** #
def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= (1 - 0.01)
        else:
            dayup *= (1 + df)
    return dayup


while dayUP(dayfactor) < ddup:
    dayfactor += 0.001
# ********** End ********** #
# 请不要修改下面的代码
print("{:.4f}.".format(dayfactor))

# 任务三：天天向上续
from math import *

Restday = 10  # 休息10天,
dayup, dayfactor = 1.0, 0.01  # 初始值
# 请在下面编写代码
# ********** Begin ********** #
restday = -3
for i in range(1, 366):
    if i % 9 == 0:
        restday = -3
    restday += 1
    if i % 10 == 0:
        restday = -3
        continue
    if restday > 0:
        dayup *= 1 + dayfactor

# ********** End ********** #
# 请不要修改下面的代码

print("{:.2f}".format(dayup))


# 第四关

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:25:23 2020

@author: hzh
"""
from math import *

# 第1题
list1 = [6, 8, 10, 20]  # n的取值列表list1
numbers = []  # 用来存放结果的


def F(n):
    a1 = 1
    a2 = 1
    n -= 1
    while n > 0:
        t = a1 + a2
        a1 = a2
        a2 = t
        n -= 1
    return a1


for n in list1:  # 依次从列表中取出数据赋值给n，求第n项的结果并保存到numbers[]列表中
    # 请在下面编写代码
    # ********** Begin ********** #
    numbers.append(F(n))
# ********** End ********** #
# 请不要修改下面的代码
print(numbers)
print('\n***********************\n')

# 第2题

numbers = []

# 请在下面编写代码
# ********** Begin ********** #
count = 0
while count <= 300:
    if count % 2 == 0 and count % 3 == 0 and count % 5 == 0:
        numbers.append(count)
    count += 1
# ********** End ********** #
# 请不要修改下面的代码
print(numbers)

print('\n***********************\n')

# 第3题：输出100以内的素数。

numbers = []  # 存放结果的列表

# 请在下面编写代码
# ********** Begin ********** #
for i in range(2, 101):
    if i == 2:
        numbers.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            numbers.append(i)

# ********** End ********** #
# 请不要修改下面的代码
print(numbers)

print('\n***********************\n')

# 第4题求：1-3！+5!-7！......(-1)n-1(2n-1)!,求前n的项的和
number = [2, 4, 5, 7, 10]  # n取值来自列表
result = []  # 存放结果的程序


def JC(n):
    if n == 1:
        return 1
    else:
        return JC(n - 1) * n


for n in number:
    # 请在下面编写代码
    # ********** Begin ********** #
    count = 0
    for i in range(n):
        x = (-1) ** (i) * JC(2 * i + 1)
        count += x
    result.append(count)
# ********** End ********** #
# 请不要修改下面的代码
print(result)

print('\n***********************\n')

# 第5题 ：求sin(x)的值
# from math import *
Number = [pi, pi / 2, pi / 4]  # x的取值
result = []

for x in Number:

    # 请在下面编写代码
    # ********** Begin ********** #
    count = 1
    all_count = 0
    while not abs(x ** (2 * count - 1) / JC(2 * count - 1)) < 10e-7:
        y = (-1) ** (count - 1) * (x ** (2 * count - 1)) / JC(2 * count - 1)
        all_count += y
        count += 1

    y = (-1) ** (count - 1) * (x ** (2 * count - 1)) / JC(2 * count - 1)
    all_count += y
    if all_count > 1:
        all_count -= y
    result.append(all_count)
# ********** End ********** #
for num in result:
    print("output=%.10f" % num)
# 请不要修改下面的代码
print('\n***********************\n')

# 第6题 #求数列队中两个数的最大公约数

Number = [(8, 6), (12, 18), (15, 8), (100, 75)]
greatcd = []  # 保存最大公约数


# 求最大公约数
def gcd(a, b):
    if a < b:
        a, b = b, a
    x = a % b
    while x:
        a = b
        b = x
        x = a % b
    return b


# 求最小公倍数
def lcm(a, b):
    x = a * b // _gcd(a, b)
    return x


for a, b in Number:
    # 请在下面编写代码
    # ********** Begin ********** #
    greatcd.append(gcd(a, b))

    # ********** End ********** #
    # 请不要修改下面的代码

print(greatcd)

print('\n***********************\n')

