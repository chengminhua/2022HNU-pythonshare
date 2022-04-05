# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年04月05日
"""
# 第一关
# coding=utf-8

# 存放姓氏和名字的变量
first_name = input()
last_name = input()

# 请在下面添加字符串拼接的代码，完成相应功能
###### Begin ######
print(first_name,last_name)

####### End #######

# 第二关
#coding=utf-8

# 获取待处理的源字符串
source_string = input()

# 请在下面添加字符串转换的代码
###### Begin ######
source_string = source_string.strip()
print(source_string.title())
print(len(source_string))
####### End #######


# 第三关
# coding = utf-8

source_string = input()

# 请在下面添加代码
###### Begin ######
print(source_string.find("day"))
new_string = source_string.replace("day","time")
print(new_string)
print(new_string.split(" "))
####### End #######

