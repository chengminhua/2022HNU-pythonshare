# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年02月28日
"""

#第1关：数据输入与输出

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:39:58 2020

@author: hzh
"""

# 第一题:在屏幕上输出字符串：hi, "how are you" ,I'm fine and you
# -------begin-------------#

print('hi, "how are you" ,I\'m fine and you')

# -------ends--------------#

# 第二题:从键盘输入两个整数，计算两个数相除的商与余数
x, y = eval(input())
# -------begin-----------
print(float(x / y), end=' ')
print((x % y))

# 第三题:在屏幕上输入一个三位数输出该数的个位、十位和百位数字
x = eval(input())
# -------begin-----------
print(x % 10, end=' ')
print((x % 100) // 10, end=' ')
print(x // 100)

# -------ends------------

# 第四题:已知a=1.234567,b=0.000321 .按保留小数点后3位输出a，2.按指数形式输出 b
a, b = 1.234567, 0.00321
# -------begin-----------
print("a={:.3f}".format(a), end=',')
print("b={:.2e}".format(b))

# -------ends------------

# 第五题:请问一个硬盘的存储容量为500GB, 请问该硬盘最多可存放多少个字节的数据量
# -------begin-----------
print(500 * 1024 * 1024 * 1024)

# -------ends------------

# 第六题:计算并判断!![,](/api/attachments/1152943)，是否大于1.01，输出判断结果True,False。
# -------begin-----------
if 1.01 ** 3 * 0.99 ** 2 > 1.01:
    print("True")
else:
    print("False")

# -------ends------------

# 第2关：表达式的计算问题
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:23:44 2020
表达式的计算问题
@author: hzh
"""
# 参考答案
from math import *


def print_(x):
    if type(x) == float:
        print("%.4f" % x)
    else:
        print(x)


# ********** Begin ********** #
# 请在每一题的print语句内完成题目所需的表达式

# 第一题
print_(pi ** 4 + pi ** 5)
print_(e ** 6)
print_(pi ** 4 + pi ** 5 - e ** 6)

# 第二题
print_(radians(45))
print_(4 * atan(1 / 5) - atan(1 / 239))

# #第三题
print_(sinh(0.25))
print_((e ** 0.25 - e ** -0.25) / 2)

# #第四题
h, v0, g, θ = 1.9, 14, 9.8, 40  # 变量赋值
θ = radians(θ)
print_((2 * v0 * sin(θ) + sqrt(4 * (v0 ** 2) * (sin(θ) ** 2) + 8 * h * g)) / (2 * g))

# #第五题
θ = eval(input())  # 输入角度值
θ = radians(θ)
print_(log(abs(cos(θ)) * exp(sin(θ)), e))

# ********** End ********** #

# 第3关：简单计算问题的求解

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:31:38 2020
 任务：计算一个由正方形和等腰三角形组成的多边形的面积，其中正方形边长4厘米
，等腰三角形底边为正方形的一条边，其到对角顶点的高为2.6厘米。
@author: hzh
"""
from math import *


def print_(x):
    if type(x) == float:
        print("%.2f" % x)
    else:
        print(x)


# 第一题：无输入求多边形的面积
square_length = 4  # 声明整型变量square_length用于表示正方形边长，并赋值 4
triangle_h = 2.6  # 声明浮点型变量triangle_h用于表示三角形底边上的高，并赋值 2.6

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 第1步：计算正方形面积，赋值给变量area_square
area_square = square_length ** 2
# 第2步：计算等腰三角形面积，赋值给变量area_triangle
area_triangle = square_length * triangle_h * 0.5
# 第3步：计算多边形面积，即正方形面积和等腰三角形面积，赋值给变量area_total
area_total = area_square + area_triangle
# 第4步：打印输出多边形面积，即使用print_()函数输出变量area_total的值
print_(area_total)
########## End ##########
print('***********************')

# 第二题：从键盘输入摄氏温度，将摄氏温度转换为华氏温度并输出
########## Begin ##########
# 第1步:给C赋值
C = input()
# 第2步：计算F的值
F = 9 * int(C) / 5 + 32
########## End ##########
print_(F)  # 输出结果

print('***********************')

# 第三题：钟形高斯函数的计算
########## Begin ##########
# 第1步:给m,s,x赋值
m, s, x = eval(input())
# 第2步:计算fx的值
fx = exp((1 / 2) * -((x - m) / s) ** 2) * (1 / (2 * pi * s) ** 0.5)
########## End ##########
print_(fx)  # 输出结果
print('***********************')

# 第四题：编写一个计算并打印地球上两点的大圆弧距离的Python程序
########## Begin ##########
# 第1步:给x1,y1,x2,y2赋值
x1, y1, x2, y2 = eval(input())
R = 69.1105
# 第2步:角度到弧度的转换
x1 = radians(x1)
y1 = radians(y1)
x2 = radians(x2)
y2 = radians(y2)
# 第3步:计算dist的值
dist = R * degrees(acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))) * 1.609
########## End ##########
print_(dist)  # 输出结果
print('***********************')

# 第4关：顺序程序设计

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:55:39 2020
程序代码 ：顺序结构程序设计 
@author: hzh
"""
from math import *


def print_(x):
    if type(x) == float:
        print("%.2f" % x)
    else:
        print(x)


# **第一题**：计算距离
G = 9.8  # 声明浮点型变量 G，用于表示重力加速度
v0 = 5  # 声明整型变量 v0, 用于表示水平初速度
# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########### Begin ###########
# 第一步：通过input函数获取输入值，将其转换为浮点型并赋值给t
t = eval(input())
# 第二步：计算水平距离，并赋值给s
s = v0 * t
# 第三步：计算垂直距离，并赋值给h
h = (1 / 2) * G * t ** 2
# 第四步：计算小球与原点的距离，并赋值给d
d = sqrt(s ** 2 + h ** 2)
# 第五步：按照保留小数点后2位格式输出小球与原点的距离d
print_(d)
########### End ###########
print('***********************')

# **第二题**：求三角形面积,结果保留小数点后2位
########### Begin ###########
a, b, c = eval(input())
p = (1 / 2) * (a + b + c)
s = sqrt(p * (p - a) * (p - b) * (p - c))
print_(s)
########### End ###########
print('***********************')

# **第三题**：逆序数输出
########### Begin ###########
x = input()
print(x[::-1])
########### End ###########
print('***********************')

# **第四题**： 对角线求点的个数，以整数输出结果
########### Begin ###########
y = eval(input())
print(int(y * (y - 1) * (y - 2) * (y - 3) / 24))

########### End ###########
print('***********************')

