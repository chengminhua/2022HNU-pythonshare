# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年11月02日
"""
list1 = []
num3 = ''
try:
    num = input("请输入一个不多于5位的正整数：")
    num2 = int(num)
    if num2>0 and len(num)<=5:
        print(f"这串数字的长度为 {len(num)}")   #输出正整数的长度
        for i in str(num):
            print(i,end='\t')                #分别输出正整数中的每个数字
            list1.append(i)
        list1.reverse()                      #正整数的反转
        print(f"\n{num3.join(list1)}")       #将反转的正整数拿出来并拼在一起，输出
    else:
        print('请输入正确格式的正整数！')
except:
    print('请输入正确格式的正整数！!')
