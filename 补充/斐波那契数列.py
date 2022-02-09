# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月31日
"""

def fib(max_count):
    count_list = []
    first_num = 1
    sec_num = 0
    count = 1
    while count<=max_count:
        add_num = first_num+sec_num
        first_num = sec_num
        sec_num = add_num
        count_list.append(add_num)
        count+=1
    return count_list

count = input("请输入要生成斐波那契数列的个数：")
count = int(count)
fib_generator = fib(count)
for num in enumerate(fib_generator,1):
    print(num)



