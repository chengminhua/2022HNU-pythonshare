# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月19日
"""
#元组一般不可变，但里面的元素若可变（比如列表），则可用append等方法改变！


n1=yuan_zu=(1,2,3,4,5,'cheng')
n2=yuan_zu2=('hua',)    #只有一个对象的时候不加个逗号就不是元组
n3=yuan_zu3=tuple('1',)      #只加一个括号也可创建tuple，但最多一个对象，且必须是str
n4=yuan_zu4=tuple((1,))      #正常的创建方式
print(n1,n2,n3,n4)
print(type(n1),type(n2),type(n3),type(n4))

for i in n1:
    print(i,end='\t')     #元组可遍历

