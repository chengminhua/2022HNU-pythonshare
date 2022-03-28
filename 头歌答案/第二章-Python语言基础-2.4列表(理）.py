# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月28日
"""

# 第一关
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:25:27 2020

@author: hyr
列表的增删改查
好友名单管理
"""
#建立初始名单
nameList=eval(input())

############begin###############
#1.请在好友名单尾部添加一个好友'曾海洋'
nameList.append('曾海洋')
############end#################



############begin############
#2.请在好友名单开头添加一个好友'胡波'
nameList.insert(0,'胡波')
##############end############


#############begin###########
#3.请将首个王姓好友的名字修改为'王仁'。
count = 0
for i in nameList:
    if i[0] == "王":
        break
    else:
        count += 1
nameList[count] = "王仁"
#############end#############


############begin################
#4.删除首个赵姓好友
count = 0
for i in nameList:
    if i[0] == "赵":
        break
    else:
        count += 1
del nameList[count]
###########end#################



print(nameList)


# 第二关
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:27:39 2020

@author: hyr
列表的排序
对一个班的学生的数学成绩进行排序，并进行简单的统
"""


scores=eval(input())#录入多名学生的成绩


#########begin############
#1. 请找出最高分并输出
max_scores = scores[0]
for i in scores:
    if i > max_scores:
        max_scores = i
print(max_scores)
##########end############




###########begin###########
#2. 请找出最低分并输出
min_scores = scores[0]
for i in scores:
    if i < min_scores:
        min_scores = i
print(min_scores)
###########end############



###########begin############
#3. 请求出班级平均分并输出(保留4位小数)
mix_scores = 0
count = 0
for i in scores:
    count += i
mix_scores = count / len(scores)
print("{:.4f}".format(mix_scores))
###########end##############



############begin###########
#4.对分数进行升序排序并输出排序后的结果
scores.sort(reverse=False)
print(scores)
############end############

# 第三关
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:32:01 2020

@author: hyr
列表索引切片
对学生成绩进行降序排序，输出前三名的成绩，以及后三名的成绩，以及去掉一个最高的去掉一个最低分之后的成绩均值。
"""

#已录入的10名学生的成绩
scores=eval(input())#录入多名学生的成绩



##########begin###########
#1. 请对scores进行降序排序，并输出降序排列之后的结果
scores.sort(reverse=True)
print(scores)
##########end#############



#########begin############
#2.请找出前三名的成绩，并按降序输出
print(scores[0:3])
##########end############




###########begin###########
#3. 请找出后三名的成绩，并按降序输出
print(scores[-3:])
###########end############



###########begin############
#4.请求出去掉一个最高分以及去掉一个最低分之后的成绩均值，并输出该均值(保留4位小数)
count = 0
for i in scores[1:-1]:
    count += i
print("{:.4f}".format(count / len(scores[1:-1])))
###########end##############



# 第四关
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 09:01:10 2021

@author: hyr
"""

row = eval(input())  # 矩阵行数
list2D = []  # 嵌套列表，用来存放一个矩阵数据
for i in range(row):  # 得到每行数据列表
    temp = eval(input())
    list2D.append(temp)

# 第1题：请对矩阵list2D中的数据求最大值,并输出该最大值
max_num = list2D[0][0]
for i in list2D:
    for j in i:
        if j > max_num:
            max_num = j
print(max_num)

# 第2题：求出矩阵对角线元素的和，并输出该和值
count = 0
lieshu = len(list2D[0])
for i in range(len(list2D)):
    for j in range(lieshu):
        if i == j:
            count += list2D[i][j]
print(count)

# 第3题：将矩阵上三角元素全变为0值, 并输出该矩阵
# 列数
lieshu = len(list2D[0])
for i in range(len(list2D)):
    for j in range(lieshu):
        if i <= j:
            list2D[i][j] = 0
for i in list2D:
    print(i)

# 第4题：取出矩阵的最后两行，并输出这两行
for i in list2D[-2:]:
    print(i)

# 第5题：删除矩阵的最后一行,并输出删除最后一行之后的矩阵
del list2D[-1]
for i in list2D:
    print(i)

# 第五关
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:03:22 2021

@author: hzh
"""

#列表综合案例1：输出杨辉三角形（列表的嵌套）
num = eval(input()) #num为杨辉三角的行数

#########begin##############
num_list = [[1],[1,1]]
if not num >= 3:
    if num == 1:
        num_list = [[1]]
else:
    for i in range(num):
        if i == 0 or i == 1 :
            continue
        else:
            new_row = [1 for j in range(i+1)]
            for x in range(1,len(new_row)-1):
                new_row[x] = num_list[i-1][x-1] + num_list[i-1][x]
            num_list.append(new_row)

for j in num_list:
    print(j)
#########ends##############

#列表综合案例2：约瑟夫问题
#n代表总人数,m代表出圈间隔序号数
n,m=eval(input())
result=[] #出圈列表
#########begin##############
lb = [i for i in range(1,n+1)]
lb = lb[::-1]
count = 0
while lb:
    for j in lb[::-1]:
        count += 1
        if count == m:
            lb.remove(j)
            result.append(j)
            count = 0

#########ends##############
####下面的代码不能修改######
print("出圈列表:")
print(result)