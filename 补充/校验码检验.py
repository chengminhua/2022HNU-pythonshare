# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年11月14日
"""
#背后的实现原理就是现实中的校验码实现原理！

num = input('请输入一个13位的校验码：')
num_1 = int(num)
# print(num_1)
s1, s2 = 0, 0  #设置初始值
a = 0   #用于确认是奇数还是偶数位上的数字
#将ISBN码一个个取出，来计算
for i in num:
    num_i = int(i)
    if a%2==0:
        s2 += num_i
        a+=1
    else :
        s1 += num_i
        a+=1
#调整误差用
s2 = s2-num_1%10
# print(s1,s2)

#也是验证的一部分，比较容易理解
r = (s2+s1*3)%10
r1 = (10-r)%10

if r1 == num_1%10 :
    print('校验成功！')
else:
    print('校验失败，请输入正确的校验码！')









