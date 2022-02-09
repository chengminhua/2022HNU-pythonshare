# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月28日
"""


#创建一个列表来装答案
answer = []
#用循环来遍历数据
for i in range(2000,3201):
#验证条件
    if i%7==0 and i%5!=0:
#将符合的数据加入到answer列表后
        answer.append(i)
    else:
        continue
#输出列表
print(answer)
#计算一共有多少个数字
print(len(answer))