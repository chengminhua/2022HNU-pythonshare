# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年10月16日
"""
for i in range(1,5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        else:
            print(j,end='\t')
    print(end='\n')  #一定要和内层循环在一排，才能换行.      print里面的东西可写可不写

