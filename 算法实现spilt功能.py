# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年01月26日
"""
"""
创建一个函数，来实现spilt功能。
主要功能：可以支持像spilt函数一样的切开字符串的功能，然后还可以选择切几次，总的来说还不错！
"""

def spilt_my(string,res,num=0):
    spilt_list = []
    begin_index = 0
    is_do = False

    if num:
        is_do = True

    for index,char in enumerate(string):
        if char == res:
            if is_do and num:
                num -= 1
            else:
                spilt_list.append(string[begin_index:])
                break
            spilt_list.append(string[begin_index:index])
            begin_index = index + 1

        elif index + 1 == len(string):
            spilt_list.append(string[begin_index:])
    return spilt_list

if __name__ == '__main__':
    print(spilt_my(input(">>>"),"-",1))
