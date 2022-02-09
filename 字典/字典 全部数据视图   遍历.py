# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月19日
"""
a={'name':'cheng','age':18,'class1':4}
n1=a.keys()     #全部key
n2=a.values()   #全部value
n3=a.items()    #全部key-value对
print(n1,n2,n3)
for v in a:
    print(v,a[v],a.get(v))     #字典的遍历