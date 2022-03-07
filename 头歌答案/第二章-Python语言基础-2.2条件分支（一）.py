# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月07日
"""
# 第一关
changeOne = int(input())
changeTwo = int(input())
plus = int(input())

#请在此添加代码，交换changeOne,changeTwo的值，然后计算changeOne和plus的和result的值
#********** Begin *********#

changeOne,changeTwo  =  changeTwo,changeOne
result = changeOne + plus


#********** End **********#
print(result)


# 第二关
workYear = int(input())
# 请在下面填入如果workYear < 5的判断语句
# ********** Begin *********#
if workYear < 5:
    # ********** End ***********#
    print("工资涨幅为0")
# 请在下面填入如果workYear >= 5 and workYear < 10的判断语句
# ********** Begin *********#
elif workYear >= 5 and workYear < 10:
    # ********** End ***********#
    print("工资涨幅为5%")
# 请在下面填入如果workYear >= 10 and workYear < 15的判断语句
# ********** Begin *********#
elif workYear >= 10 and workYear < 15:
    # ********** End ***********#
    print("工资涨幅为10%")
# 请在下面填入当上述条件判断都为假时的判断语句
# ********** Begin *********#
else:
    # ********** End ***********#
    print("工资涨幅为15%")


# 第三关
jimscore = int(input())
jerryscore = int(input())
#请在此添加代码，判断若jim的得分jimscore更高，则赢家为jim。若jerry的得分jerryscore更高，则赢家为jerry并输出赢家的名字。
#********** Begin *********#

winner = "jim" if jimscore > jerryscore else "jerry"


#********** End **********#
print(winner)


# 第四关
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:49:20 2020

@author: hzh
"""
# 第一题
month_list = [1,3,5,7,8,10,12]
month = int(input())
# 31天的月份：1~7之间的奇数月、8~12之间的偶数月
# 如果是31天的月份输出yes
####### begin #######
if month in month_list:
    print("yes")
else:
    print("no")

####### end #########
# 如果不是31天的月份，输出no
####### begin #######

####### end #########
print('\n***********************\n')

#第二题
# 从测试集得到风速
velocity = int(input())
# 默认是0级
rank = 0
# 如果风速在74到95之间，输出1
####### begin #######
if 74<=velocity<=95:
    rank = 1
####### end #########
# 如果风速在96到110之间，输出2
####### begin #######
if 96<=velocity<=110:
    rank = 2
####### end #########
# 如果风速在111到130之间，输出3
####### begin #######
if 111<=velocity<=130:
    rank = 3
####### end #########
# 如果风速在131到154之间，输出4
####### begin #######
if 131<=velocity<=154:
    rank = 4
####### end #########
# 如果风速大于155，输出5
####### begin #######
if velocity>=155:
    rank = 5
####### end #########
print(rank)



