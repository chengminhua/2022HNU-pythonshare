# 第一题
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:36:42 2020

@author: Administrator
"""

# 创建并初始化score_dict字典
score_dict = {}
for i in range(5):
    # 请按下面的注释提示添加代码，完成相应功能
    #1.对score_dict字典进行初始化，数据从键盘输入，得到如任务描述中的字典
    ###### Begin ######
    course = input()
    number = input()
    if number.isdecimal():
        number = int(number)
    score_dict[course] = number
    #######  End #######


# 请按下面的注释提示添加代码，完成相应功能
#2.请在此添加代码，实现对score_dict的添加、删除、查找、修改等操作，并打印输出相应的值
###### Begin ######
score_dict["体育"] = 90
if not score_dict.get("化学", 0):
    print("不存在")
else:
    print(score_dict.get("化学"))

score_dict["语文"] = 100

del score_dict["信息"]

print(score_dict)
#######  End #######

# 第二题
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:36:42 2020

@author: Administrator
"""

# 创建并初始化score_dict字典
score_list=['姓名','语文','英语','数学','体育']
# 请按下面的注释提示添加代码，完成相应功能
#1.根据上面的列表创建score_dict字典并初始化，得到如任务描述中的字典，字典中的值从键盘输入
###### Begin ######
score_dict = {}
count = 0
for i in score_list:
    num = input()
    if num.isdecimal():
        num = int(num)
        count += num
    score_dict[i] = num
score_dict["总分"] = count
#######  End #######


# 请按下面的注释提示添加代码，完成相应功能
#2.请在此添加代码，计算张三同学的总分，并将总分作为新的键值对加入，最后输出score_dict的所有键值对
###### Begin ######
for i,j in score_dict.items():
    print(i,j)
#######  End #######


# 第三题
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:36:42 2020

@author: Administrator
"""

# 创建空列表score_dict
score_dict = {}
# 每次循环生成一个键值对
for i in range(3):
    # 输入课程名作为字典的键
    key = input()
    # 创建空列表
    value_list = []
    # 请按下面的注释提示添加代码，完成相应功能
    # 1.从键盘输入两个分数，保存到列表中
    ###### Begin ######
    num1 = eval(input())
    num2 = eval(input())
    value_list.append(num1)
    value_list.append(num2)
    #######  End #######
    score_dict[key] = value_list

print(score_dict)

# 创建空列表score_list
score_list = []
# 每次循环生成一个字典
for i in range(2):
    # 创建空字典
    s_dict = {}
    # 请按下面的注释提示添加代码，完成相应功能
    # 2.对从键盘输入三门课程及成绩，保存到字典中
    ###### Begin ######
    for i in range(3):
        key = input()
        num = eval(input())
        s_dict[key] = num

    #######  End #######
    score_list.append(s_dict)

print(score_list)


# 第四题
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:43:33 2021

@author: hzh
"""
# 输入的字符串中可包含".,~!@#$%^&*()+_/0123456789"等非英文单词字符
WordStr = input()
# stpe1:归一化处理

fuhao = """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
for i in fuhao:
    WordStr = WordStr.replace(i, " ")

# 2分割字符串为列表,英文单词之间用空格分隔
WordStr_list = WordStr.split(" ")
WordStr_dict = {}

# 3 统计每个单词的个数（列表或字典的方法）
for j in WordStr_list:
    j = j.strip().lower()
    if len(j) != 0:
        if not WordStr_dict.get(j, 0):
            WordStr_dict[j] = 1
        else:
            WordStr_dict[j] = WordStr_dict.get(j) + 1

# print(WordStr_dict)
show_list = []
max_num = 0
for key, value in WordStr_dict.items():
    if value > max_num:
        show_list.clear()
        show_list.append(key)
        max_num = value
    elif value == max_num:
        show_list.append(key)
    else:
        continue

# show_list.sort()
for j in show_list:
    print(j, max_num)

# 字典排序,返回值是一个列表


# 输出最高频率单词和次数 ,多个相同高频字也要输出


# 第五题
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:03:33 2021
 整数的翻译
@author: hzh
"""


# 数字翻译成英文程序
def unit_to_word(u):  # 将0～9的数字转换成英文，并返回转换后的英文
    # 请在下面编写代码
    # ********** Begin ********** #
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    return num_list[u]

    # ********** End ********** #
    # 请不要修改下面的代码


def tens_to_word(t):  # 利用unit_to_word，将10～19、
    # 以及20～99的十位部分数字转换成英文，并返回转换后的英文
    # 请在下面编写代码
    # ********** Begin ********** #
    num_list_10_to_19 = ["ten", "eleven", 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                         'eighteen', 'nineteen']
    num_list_zhengshu = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
    if 20 <= t <= 99:
        need_return_str = ""
        t_str = str(t)
        first = t_str[0]
        secend = t_str[1]
        if secend != "0":
            need_return_str = num_list_zhengshu[int(first) - 2] + " " + unit_to_word(int(secend))
        else:
            need_return_str = num_list_zhengshu[int(first) - 2]
    else:
        need_return_str = num_list_10_to_19[t - 10]

    return need_return_str
    # ********** End ********** #
    # 请不要修改下面的代码


def hundreds_to_word(h):  # 利用unit_to_word、tens_to_word进行转换，并返回转换后结果的函数
    # 请在下面编写代码
    # ********** Begin ********** #
    new_str = ""
    if h <= 9:
        str1 = unit_to_word(h)
        return str1
    elif 10 <= h <= 99:
        str1 = tens_to_word(h)
        return str1
    else:
        h1 = h // 100
        h2 = h % 100
        new_str = unit_to_word(h1) + " hundred and " + tens_to_word(h2)
        return new_str
    # ********** End ********** #
    # 请不要修改下面的代码


test = eval(input())
print(test, "==>", hundreds_to_word(test))
