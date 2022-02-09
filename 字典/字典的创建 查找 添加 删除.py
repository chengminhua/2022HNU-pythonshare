# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月19日
"""
a={'name':'cheng','age':18,'class1':4}        #字典的创建   key不能重复
print(a,type(a))
b=dict(name='cheng',age=18)      #字典的创建
print(b,type(b))
print(a['name'])     #查找字典中的key，若找不到则返回keyError   查找value
print(a.get('name',99))
print(a.get('class12',99))    #另一种查找的方法，若没有则返回None或‘，’后面的值    查找value


print('name' in a)
print('hh' not in a)   # in 或 not in 判断 某个key在不在字典中

del a['name']    #删除
print(a)
a['华']='hua'       #添加可以-value对
print(a)

