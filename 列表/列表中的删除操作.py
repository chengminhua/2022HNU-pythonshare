# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月17日
"""
list1=[1,1,2,3,4,5,6,7,8,9,0]
list1.remove(1)    #输入列表中指定的value来删除，一次一个，如果有多个就删除第一个
print(list1,id(list1))
list1.pop()   #只能删除一个，如果不填数字那就删最后一个
print(list1,id(list1))
list2=list1[1:3]     #切片操作只是拿出原列表的数据，不会对原列表做出变动    会对内存地址发生改变
print(list2,id(list2))
print('原列表',list1,id(list1))


list3=[10,20,30,40,50,60,70,80,90]
list3[0:3]=[]                        #切片操作同样是左取右不取     这行的意思是切掉原列表的数据且不建立新的列表
print(list3)
list3.clear()                 #清空列表
print(list3)


del list3            #直接删除列表
print(list3)