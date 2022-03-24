# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月24日
"""

# 第一题
n = eval(input())

count = 0
for i in range(1, n + 1):
    count += ((-1) ** (i - 1)) * ((2 * i - 1) ** 2)

print(count)


# 第二题
n = eval(input())

count = 0

for i in range(1,n+1):
    for j in range(1,i+1):
        count += j

print(count)

# 第三题
max_ = 0
mix_ = 0
count = 0
n = 0
while 1:
    x = eval(input())
    if x > 0:
        if x > max_:
            max_ = x
        count += x
        n += 1
    else:
        break
if not n == 0:
    mix_ = count / n
    print("最高分：{:.2f}，平均分：{:.2f}".format(max_,mix_))
else:
    print("输入无效")


# 第四题
x = eval(input())
while x != 1:
    if x % 2 == 0:
        print("{}/2={}".format(int(x),int(x/2)))
        x = x / 2
    else:
        print("{}*3+1={}".format(int(x),int(3*x+1)))
        x = 3*x+1

