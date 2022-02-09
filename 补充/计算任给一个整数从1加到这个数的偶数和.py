# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月16日
"""
'''计算1-100之间的偶数和'''
sum=0
a=1
b=int(input('请输入一个整数：'))
while a<=b:
    if not bool(a%2):
        sum+=a
        a+=1
    else:
        a+=1
print(sum)
