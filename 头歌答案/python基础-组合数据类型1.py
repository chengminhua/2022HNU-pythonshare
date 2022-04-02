# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年04月02日
"""

# 第一关
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:39:09 2020

@author: jerry
"""

# 题1：有如下列表，按照要求实现每一个功能
li = ["Witharush", "eric", "rain", "aa", "bb", "cc", "dd"]
############begin###############
# a.计算列表长度并输出
print(len(li))
############end#################

############begin###############
# b.列表中追加元素"seven"，并输出添加后的列表
li.append("seven")
print(li)
############end#################

############begin###############
# c.请在列表的第2个位置插入元素"Tony"，并输出添加后的列表
li.insert(1, "Tony")
print(li)
############end#################

############begin###############
# d.请修改列表的第1个位置的元素为"Kelly"，并输出修改后的列表
li[0] = "Kelly"
print(li)
############end#################

############begin###############
# e.请删除列表中的元素"eric",并输出修改后的列表
li.remove("eric")
print(li)
############end#################

############begin###############
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
ret = li.pop(1)
print(ret, li)

############end#################

############begin###############
# g.请删除列表中的第3个元素,并输出删除元素后的列表
del li[2]
print(li)
############end#################

############begin###############
# h.请删除列表中的第2至3两个元素，并输出删除元素后的列表
del li[1:3]
print(li)
############end#################

############begin###############
# i.请将列表所有的元素反转，并输出反转后的列表
li.reverse()
print(li)
############end#################

############begin###############
# j.请使用for，len，range输出列表的索引
for i in range(len(li)):
    print(i)
############end#################

############begin###############
# k.请使用enumerate输出列表元素和序号
print(list(enumerate(li)))
############end#################

############begin###############
# l.请使用for循环输出列表的所有元素
for k in li:
    print(k)
############end#################

# 第二关
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 21:40:31 2020

@author: Administrator
"""

month = int(input())
############begin###############
# 补充程序
if month in [12,1,2]:
    print("winter")
elif month in [3,4,5]:
    print("spring")
elif month in [6,7,8]:
    print("summer")
elif month in [9,10,11]:
    print("fall")
else:
    print("error")
############end#################

# 第三关
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 21:41:48 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:39:03 2020

@author: jerry
"""

m = eval(input())
li = eval(input())
############begin###############
# 补充程序
has = False
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] + li[j] == m:
            print(li[i], li[j])
            has = True

if not has:
    print("not found")

############end#################


# 第四关
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 21:21:12 2020

@author: Administrator
"""

n=eval(input())
li=[]
############begin###############
# 补充程序
def JC(n):
    if n == 1:
        return 1
    else:
        return JC(n-1)*n

for i in range(n):
    x = (-1)**(i) * JC(2*i+1)
    li.append(x)
############end#################
print(sum(li))