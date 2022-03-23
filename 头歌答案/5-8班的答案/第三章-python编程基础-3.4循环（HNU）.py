# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月23日
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

######### end####
print(s)

########## 第2题 ##############
x = int(input())

if x < 0:
    print('无实数解')
else:
    g = x / 2
    #######begin##############
    # 请输入while循环控制语句
    eps = 1e-6
    while abs(x - g * g) > eps:
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
"""
Created on Tue Sep  8 07:57:31 2020

@author: hzh
"""


# 第一题
# 定义一个求第n项斐波那契数的函数
def fibNumber(n):
    # 函数说明
    # 参数n为第n项斐波那契数,第1,2项为1,1
    # 返回第n项值
    # ********** Begin ********** #
    a1 = 1
    a2 = 1
    n -= 1
    while n > 0:
        t = a1 + a2
        a1 = a2
        a2 = t
        n -= 1
    return a1

    # ********** End ********** #


# 请不要修改下面的代码
m = int(input())
print(fibNumber(m))
print(20 * '*' + '\n', end='')

# 第二题：可试着用非函数的方式写程序，注意输出数据格式
n = eval(input())
# 请在下面编写代码
# ********** Begin ********** #
count = 0
while count <= n:
    if count % 2 == 0 and count % 3 == 0 and count % 5 == 0:
        print(count, end=" ")
    count += 1

# ********** End ********** #
print('\n' + 20 * '*' + '\n', end='')


# 第三题
# 定义一个判断x是否是素数的程序
def isPrime(x):
    # 函数说明：
    # 参数x为>=2的整数
    # 返回值为1或0
    # ********** Begin ********** #
    if x == 2:
        return 1
    else:
        for j in range(2, x):
            if x % j == 0:
                return 0
        else:
            return 1
    # ********** End ********** #


# 请不要修改下面的代码
N = int(input())
# 求0-N之间的素数并输出，注意数据的输出格式
# ********** Begin ********** #
for i in range(2, N):
    if isPrime(i):
        print(i, end=" ")

# ********** End ********** #
print('\n' + 20 * '*' + '\n', end='')


# 第四题
# 定义一个求两个数的最大公约数的函数
def gcd(a, b):
    # 函数说明
    # 参数a,b为两个整数，并且a>b
    # 返回两个数的最大公约数
    # ********** Begin ********** #
    if a < b:
        a, b = b, a
    x = a % b
    while x:
        a = b
        b = x
        x = a % b
    return b

    # ********** End ********** #
    # 请不要修改下面的代码


m, n = eval(input())
# 函数调用求最大公约数保存在gcdnum中
# ********** Begin ********** #
gcdnum = gcd(m, n)

# ********** End ********** #
print("最大公约数：%d" % gcdnum)
print("最小公倍数：%d" % ((m * n) / gcdnum))
print(20 * '*', end='')


# 第四关
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 21:24:02 2021

@author: hzh
"""
# 第1题：用循环的方式求π/4≈ 1-1/3+1/5-1/7+......直到最后一项绝对值小于1e−6（即10−6）为止，保留小数点后10位
import math

# ********** Begin ********** #
S = 0
n = 1
eps = 1e-6
while 1 / (2 * n - 1) > eps:
    S += ((-1) ** (n - 1)) / (2 * n - 1)
    n += 1
# ********** End ********** #
# 请不要修改下面的代码
# print("数列和为：%.10f" % S )
print("数列和为：{:.10f}".format(S))


# 0.7853976634

# 第2题求：1-3！+5!-7！......(-1)n-1(2n-1)!,求前n的项的和
# 函数定义求前n项数列和
def sumSequ(n):
    # 函数说明
    # 参数n为数列前n项
    # 返回前n项的和
    # 请在下面编写代码
    # ********** Begin ********** #
    def JC(n):
        if n == 1:
            return 1
        else:
            return JC(n - 1) * n

    count = 0
    for i in range(n):
        x = (-1) ** (i) * JC(2 * i + 1)
        count += x
    return count

    # ********** End ********** #


# 请不要修改下面的代码
m = int(input())  # 从键盘输入 m值
s = sumSequ(m)  # 函数调用求数列和
print("数列前%d项的和为%d" % (m, s))

# 第3题
from math import *


def calSinx(x):
    # 函数说明：
    # 参数x为弧度值
    # 返回数列和的结果，保留小数点后10位
    # 请在下面编写代码
    # ********** Begin ********** #
    def JC(n):
        if n == 1:
            return 1
        else:
            return JC(n - 1) * n

    count = 1
    all_count = 0
    while not abs(x ** (2 * count - 1) / JC(2 * count - 1)) < 1e-7:
        y = (-1) ** (count - 1) * (x ** (2 * count - 1)) / JC(2 * count - 1)
        all_count += y
        count += 1
    return all_count
    # ********** End ********** #


# 请不要修改下面的代码
theta = eval(input())  # 输入角度值
x = radians(theta)
Sx = calSinx(x)
print("output=%.10f" % (Sx))


# 第五关
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:49:56 2020

@author: hzh
"""
from math import *

#任务一：三天打鱼两天晒网
dayup, dayfactor = 1.0, 0.01
  #请在下面编写代码
  # ********** begin ********** #
dayup = (dayup - dayfactor) ** 146 * (dayup + dayfactor) ** 219

  # ********** End ********** #
   # 请不要修改下面的代码
print("{:.2f}.".format(dayup))


#任务二：天天向上的力量
import math
dayup, dayfactor = 1.0, 0.01
ddup= math.pow((dayup+dayfactor),365)
# print("天天向上的力量: {:.2f}.".format(ddup)) 37.78
    #请在下面编写代码
# ********** Begin ********** #
def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= (1-0.01)
        else:
            dayup *= (1+df)
    return dayup

while dayUP(dayfactor) <= ddup:
    dayfactor += 0.001
# ********** End ********** #
    # 请不要修改下面的代码
print("{:.4f}.".format(dayfactor))


#任务三：天天向上续
from math import *
Restday = 10 #休息10天,
dayup, dayfactor = 1.0, 0.01 #初始值
 #请在下面编写代码
# ********** Begin ********** #
restday = -3
j = 0
for i in range(1,366):
    j += 1
    if j % 8 == 0:
        j = 1
        restday = -3
    restday += 1
    if i % 10 == 0:
        j = 0
        restday = -3
        continue
    if restday > 0:
        dayup *= 1 + dayfactor


# ********** End ********** #
    # 请不要修改下面的代码

print("{:.2f}".format(dayup))

