# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月16日
"""
import sys
import os
number=123456
money=1000
d=0
while d<3:  #输入密码 3次机会
    number2=int(input('请输入密码:'))
    if number!=number2:
        d += 1
        print('密码错误，你还剩'+str(3-int(d))+'次机会')   #提示还有几次机会

        if d==3:
            print('忘了密码还取钱？？？？')
            os.system('pause')
    else:
        d=3
        print('密码正确')

c=0   #取钱系统+回馈还剩多少钱
while c<3:
    a = int(input('您还剩1000元，请输入取款金额：'))
    if a<=1000:
        b=money-a
        print('剩余金额：',str(b))
        print('剩余金额：'+ str(b))
        break
    else:
        print('没那么多钱')
        c+=1
else:
    print('不想取钱就爬')

os.system('pause')  #防止.exe文件闪退
