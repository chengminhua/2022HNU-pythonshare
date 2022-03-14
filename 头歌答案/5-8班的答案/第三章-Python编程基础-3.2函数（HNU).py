# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月14日
"""
# 第一关
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:31:08 2021

@author: hzh
"""
# 根据提示信息，在空位补充代码，编写下列程序：
import math


# 定义函数返回两个点的距离
def calTwodist(x1, y1, x2, y2):
    # 函数说明
    #   根据参数值计算两个点的距离
    #   :param x1:第一个点的横坐标
    #   :param y1:第一个点的纵坐标
    #   :param x2:第二个点的横坐标
    #   :param y2:第二个点的纵坐标
    #   :return: Dist两个点的距离

    ##########begin################
    # 从此开始计算两个点的坐标值
    Dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 返回两个点的坐标
    return Dist


##########ends################

#########主程序begin##########
# 从键盘输入两个点的坐标值
x1, y1, x2, y2 = eval(input())
# 函数调用求解两个点的距离
s = calTwodist(x1, y1, x2, y2)
# 输出两个点的距离，保留小数点后4位
print("result={:.4f}".format(s))

##########ends################

# 第二关
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:04:39 2021
@author: hzh
"""

# 根据提示信息，在空位补充代码，编写下列程序：
# 1、定义一个判断是否是三角形的函数，IsTriange(a,b,c),此函数已经给出答案
# 其中a,b,c为三角形三条边，如果是返回1，否则返回0

import math


def IsTriange(a, b, c):
    # 函数说明
    #   根据参数值判断是否是三角形的函数
    #   :param a:三角形一条边的长度
    #   :param b:三角形一条边的长度
    #   :param c:三角形一条边的长度
    #   :return: 0或1

    # 程序代码已经给出请认真阅读
    ##########begin################
    t1 = (a + b) > c and (a + c) > b and (b + c) > a
    t2 = (a - c) < b and (a - b) < c and (b - c) < a
    if (t1 and t2):
        return 1
    else:
        return 0

    ##########ends################


# 定义一个计算三角形的面积的函数，TriArea(a,b,c),
# 其中a,b,c为三角形三条边,如果构成三角形，返回三角形的面积，否则返回0
def TriArea(a=3, b=4, c=5):  # 设置默认参数
    ##########begin################
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


##########ends################

# 3、从键盘输入任意的a,b,c 按位置调用函数实现计算三角形面积的函数，如果不能构成三角形，返回0，否则输出三角形面积。
##########begin################
a, b, c = eval(input())
if IsTriange(a, b, c):
    print("三角形面积：{:.4f}".format(TriArea(a, b, c)))
else:
    print("三角形面积：0.0000")

##########ends################
print('*' * 20)  # 输出20个*
# 4、按默认参数调用函数计算三角形的面积，保留小数点后4位
##########begin################
print("三角形面积：{:.4f}".format(TriArea()))
##########ends################
print('*' * 20)  # 输出20个*
# 5、设置关键字参数调用函数计算(c=10,b=20,a=15)三角形的面积
##########begin################
print("三角形面积：{:.4f}".format(TriArea(c=10, b=20, a=15)))
##########ends################
print('*' * 20)  # 输出20个*

# 6、计算多边形阴影部分面积，保留小数点后4位
##########begin################
print("多边形面积为：{:.4f}".format(TriArea(9.8, 9.3, 6.4) - TriArea(2.9, 4.1, 4.7) + TriArea(2, 1.4, 2.3)))

##########ends################
print('*' * 20)  # 输出20个*


# 第三关
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:57:19 2021

@author: hzh
"""

# 定义2个lambda函数，求两个数的最大值max1,和最小值min1的函数
##########begin##########
max1 = lambda x1, x2: x1 if x1 > x2 else x2
min1 = lambda x1, x2: x1 if x1 < x2 else x2
##########ends##########

# 从键盘输入3个数，调用max1和min1函数完成求3个数的最大值和最小值的程序，输出最大值和最小值
##########begin##########
a, b, c = eval(input())
t1_max = max1(max1(a, b), c)
t2_min = min1(min1(a, b), c)
print(t1_max, t2_min)

##########ends##########


# 第四关
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:34:21 2021

@author: hzh
"""


# 定义一个计算银行本息函数
def moneyrate1(pays, rate, year):
    # 函数说明
    #
    #   根据参数值计算存款本息值
    #   :param pays:本金
    #   :param rate:利率
    #   :param year:年份
    #   :return: 本息和

    ##########begin##########
    return pays * (rate + 1) ** year


##########ends##########

# 调用moneyrate1函数计算从键盘输入的本金存1年，3年和5年的本息和并输出结果
##########begin##########
pays = eval(input())
rate_list = [0.0175, 0.0275, 0.0275]
count = 0
for i in rate_list:
    count += 1
    print("{}年的本息和为{:.4f}".format(2 * count - 1, moneyrate1(pays, i, 2 * count - 1)))

##########ends##########


# 第五关
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:53:16 2021

@author: hzh
"""


# 1定义一个判断一个数是否是素数的函数，如果是输出1，否则输出0
#######begin########
def isPrime(x):
    if x == 2:
        return 1
    for i in range(2, x):
        if x % i == 0:
            return 0
    else:
        return 1


#######ends########

# 2调用isprime()函数求两位数内的绝对素数并输出
#######begin########
for i in range(1, 10):
    for j in range(1, 10):
        if isPrime(10 * i + j) and isPrime(j * 10 + i):
            print("{}和{}是绝对素数".format(10 * i + j, j * 10 + i))

#######ends########
print('*' * 20)


# 3定义一验证歌德巴赫猜想函数
def Goldbach(N):  # 将N分解成两素数之和
    if N < 6 or N % 2 == 1:  # 若N小于6或N为奇数
        print('N应该是大于等于6的偶数')
    else:
        # 循环判断，得到符合要求的小于N的两个素数，并打印
        for x in range(2, N // 2 + 1):  # 想想为什么是从2到N/2
            # 调用isPrime函数得到符合要求的小于N的两个素数
            ######## begin ###########
            if isPrime(x) and isPrime(N - x):
                ######## end ###########
                print(N, '=', x, '+', N - x)
                break


for num in [88, 68, 50, 1000]:
    Goldbach(num)
print('*' * 20)


# 第六关
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:40:28 2021

@author: hzh
"""


# 1题 ：信用卡的验证程序
def validCreditCard(num):
    # 请在下面编写代码
    # ********** Begin ********** #
    num_list = list(str(num))
    num_list = num_list[::-1]
    sum1 = 0
    sum2 = 0
    for i in range(0, len(num_list), 2):
        sum1 += int(num_list[i])
    for j in range(1, len(num_list), 2):
        sum2 += int(num_list[j] * 2)
    if (sum1 + sum2) % 10 == 0:
        valid = True
    else:
        valid = False
    # ********** End ********** #
    return valid
    # 请不要修改下面的代码


for num in [1234567, 43589795, 87539319, 123456789]:
    valid = validCreditCard(num)
    print(valid)
print('*' * 20)


# 2题：打印日历

def day(y, m, d):  # 计算y年m月d日是星期几
    # 请在下面编写代码
    # ********** Begin ********** #
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    # ********** End ********** #
    # 请不要修改下面的代码
    return d0


def isLeapYear(year):  # 判断year年是否闰年
    # 请在下面编写代码
    # ********** Begin ********** #
    if (year % 4 == 0 and year % 100 != 0) or year * 400 == 0:
        isLeapYear = 1
    else:
        isLeapYear = 0

    # ********** End ********** #
    # 请不要修改下面的代码
    return isLeapYear


def calendar(y, m):  # 打印y年m月日历
    print('       {}年{}月'.format(y, m))
    print('Su\tM\tTu\tW\tTh\tF\tSa')
    # 请在下面编写代码调用函数计算y年m月1日是星期几保存在变量date中
    # ********** Begin ********** #
    date = day(y, m, 1)
    # print("星期：",date)
    # ********** End ********** #

    days = 0  # 初始化y年m月的天数为0
    # 请在下面编写代码计算y年m月的天数
    # ********** Begin ********** #
    big_month = [1, 3, 5, 7, 8, 10, 12]
    if isLeapYear(y):
        if m == 2:
            days = 29
        elif m in big_month:
            days = 31
        else:
            days = 30
    else:
        if m == 2:
            days = 28
        elif m in big_month:
            days = 31
        else:
            days = 30
    # ********** End ********** #
    count = date  # y年m月1日是星期几
    for i in range(date):
        print('\t', end='')
    for d in range(1, days + 1):
        print(str(d) + '\t', end="")
        count = (count + 1) % 7
        if count == 0:
            print()
    print()

    # 请不要修改下面的代码


for (y, m) in [(2017, 8), (2017, 10), (2015, 8), (2017, 2), (2016, 2)]:
    calendar(y, m)
    print('-' * 27)


