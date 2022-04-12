# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年04月11日
"""

# 第一关
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:23:19 2020

@author: hyr
拼接，统计字数，将空格改为换行，查找子串，
"""

songs = input()  # 仅包含空格和中文

##############begin###########
# 1. songs中存放的字符串仅包含空格和中文，请统计字符串变量songs中中文字的数量，直接将统计结果输出
count = 0
for j in songs:
    if j != " ":
        count += 1

print(count)

#############end##############



# 第二关
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:23:19 2020

@author: hyr
拼接，统计字数，将空格改为换行，查找子串，
"""

songs = input()  # 歌曲歌词，仅包含空格和中文
title = input()  # 歌曲标题

##############begin###########
# 1. 将songs中的空格改为换行。注意：首尾空格应去掉不用替换成换行符，连续的空格仅替换为一个换行符
songs_list = []
songs = songs.strip()
x = 0
for j in songs:
    if j == " " and x == 0:
        songs_list.append("\n")
        x += 1
    else:
        if not j == " ":
            songs_list.append(j)
            x = 0
print(title)
print("".join(songs_list))
# 2. 将title作为歌曲的首行显示，输出整首歌曲

##############end##########

# 第三关
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:23:19 2020

@author: hyr
拼接，统计字数，将空格改为换行，查找子串，
"""

songs = input()  # 仅包含空格和中文字

################begin#############
# 1. 输出songs中出现最多的一个中文字，并输出该字出现次数。
# 注意：如果有多个字出现次数相同，请以原文本中最先出现的那个为准。
songs_dic = {}

for j in songs:
    if not j == " ":
        if not songs_dic.get(j):
            songs_dic[j] = 1
        else:
            songs_dic.update({j: songs_dic.get(j) + 1})

max_num = 0
max_zi = ""
for key, value in songs_dic.items():
    if value > max_num:
        max_num = value
        max_zi = key

print(max_zi, max_num)

################end#############


# 第四关
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:23:19 2020

@author: hyr
拼接，统计字数，将空格改为换行，查找子串，
"""

songs = input()  # 仅含空格和中文的歌词字符串

######begin##################
# 1. 将songs按空格分割成一个字符串列表
# 提示，可用字符串的split函数
songs_list = songs.split(" ")

#######end##################


#############begin####################
# 2. 以上面的字符串列表为基础，找出最长的那一个字符串，以它为长度基准，其它字符串居中对齐左补中文句号。按行输出整首歌曲。
# 对齐公式：(最长行的长度-当前行的长度)//2为左补句号数
# 同学们可以自行发挥，完成本任务
longest = 0
for k in songs_list:
    if len(k) > longest:
        longest = len(k)

for k in songs_list:
    if not (k == " " or k == "\n" or len(k) == 0):
        print("。" * int((longest - len(k)) / 2) + k)

####################end#################

