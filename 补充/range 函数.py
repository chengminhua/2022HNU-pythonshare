# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月16日
"""
for i in range(6):
    s=range(6)
    print(i,type(i))   #类型为int
    print(6 in s,0 in s)   #直接用i不行，要像第7行赋个值
for v in range(1,6):
    k=range(1,6)
    print(v)
    print(list(k))    #变相不让range函数换行
