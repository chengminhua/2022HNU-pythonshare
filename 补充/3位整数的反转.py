# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月15日
"""
c=0
while c<3:
    a = int(input('请输入一个3位整数：'))
    b = len(str(a))
    if b!=3:
        print('输入的数据不是3位数，请重新输入')
        c+=1
    else:
        n1=a//100
        n2=a//10-n1*10
        n3=a-n1*100-n2*10
        print(str(n3)+str(n2)+str(n1))
        break
else:
    print('拜拜')