# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月19日
"""
# 两种创建dict的方法


name = ['qiu', 'wang', 'cheng', 'li']
age = [16, 17, 18, 19]
nn = {item.upper(): value for item, value in zip(name, age)}  # 1
print(nn)
pp = zip(name, age)  # 2
print(dict(pp))
