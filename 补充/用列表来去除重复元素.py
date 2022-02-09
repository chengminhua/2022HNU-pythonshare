# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年11月15日
"""
sort_list = []
rubbish_list = []
turn_list = []

#让用户来输入任意值来填充列表
while True:
    a = input("请输入任意东西来填充列表(Q/q退出)：")
    if a.upper() == 'Q':
        break
    else:
        if a.isdecimal():    #转变为int类型
            a=int(a)
            sort_list.append(a)
        else:
            sort_list.append(a)


print('现在的列表是{}'.format(sort_list))

#使列表中的元素不重复
"""主要思路就是创建3个列表，
一个待去重的列表，
一个接受重复元素的列表，
一个是没有重复元素的列表，
最后再赋值回去。"""
for i in range(len(sort_list)-1,-1,-1):   #从后往前取出元素
    # ele = sort_list[i]
    ele_1 = sort_list.pop(i)    #将取出的元素赋值给ele_1
    if ele_1 in sort_list:      #判断取出ele_1后的列表中还有没有ele_1这个元素
        rubbish_list.append(ele_1)   #有就把该元素扔进”垃圾箱“
    else:
        turn_list.append(ele_1)     #没有就放到中转列表中

turn_list.reverse()     #列表反转，主要是让上下列表看着统一
sort_list = turn_list    #赋值回去
print('调整后的列表是{}'.format(sort_list))    #输出
