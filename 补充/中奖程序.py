# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月21日
"""
import os
demo=[12,4,5,2,56,57,89,46,63,52,16,1,9,0,8,7]

c=0
while c<3:
    a = int(input('请输入一个100以内的整数来抽奖：'))

    if a in demo:
        print('恭喜中奖！')
        c=3
    else:
        print('未中奖，您还有'+str(2-c)+'次机会')
        c+=1

os.system('pause')