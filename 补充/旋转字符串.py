# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年11月02日
"""
#1：用切片操作来切字符串

sam = input("请输入一串字符串：")
sam_len = len(sam)
try:
    offset = int(input("请输入一个正整数来决定将多少字符串移动到后面："))
    if offset>=0:
        offset_num = offset%sam_len   #防止输入的数字大于总字符串长度
        #分别截出两段字符串
        cutstr = sam[:offset_num]
        recutstr = sam[offset_num:]

        #拼接+描述
        print(recutstr+cutstr)
        print(f"\n您输入的字符串是{sam},您希望转换的字符串位数（经过处理的）为{offset_num}")
    else:
        print('请输入正确格式的offest')
except:
    print('请输入正确格式的offest')



