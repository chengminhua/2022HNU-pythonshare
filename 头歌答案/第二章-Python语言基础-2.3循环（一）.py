# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年03月14日
"""

# 第一关
partcount = int(input())
electric = int(input())
count = 0
# 请在此添加代码，当count < partcount时的while循环判断语句
# ********** Begin *********#
while count < partcount:
    # ********** End **********#
    count += 1
    print("已加工零件个数:", count)
    if (electric):
        print("停电了，停止加工")
        # 请在此添加代码，填入break语句
        # ********** Begin *********#
        break
        # ********** End **********#

# 第二关
# 第一题
L = [101, 25, 38, 29, 108, 121]
N = len(L)
miu = sum(L)/N
s2 = 0
####### Begin #########
# 请在此输入for循环表达式
for x in L:
####### End ########
     s2 = s2+(x-miu)**2
sigma=(s2/N)**0.5
print(sigma)

# 第二题
####### Begin #########
# 请在此输入for循环表达式
for x in range(100,1000):
####### End ########
    x1 = x%10       #取出x的个位
    x2 = x//10%10   #取出x的十位
    x3 = x//100     #取出x的百位
    if x1**3+x2**3+x3**3==x:
        print(x)

# 第三关
absencenum = int(input())
studentname = []
inputlist = input()
for i in inputlist.split(','):
    result = i
    studentname.append(result)
count = 0
# 请在此添加代码，填入循环遍历studentname列表的代码
# ********** Begin *********#
for student in studentname:
    # ********** End **********#
    count += 1
    if (count == absencenum):
        # 在下面填入continue语句
        # ********** Begin *********#
        continue
        # ********** End **********#
    print(student, "的试卷已阅")

# 第四关
studentnum = int(input())
# 请在此添加代码，填入for循环遍历学生人数的代码
# ********** Begin *********#
for student in range(studentnum):
    # ********** End **********#
    sum = 0
    subjectscore = []
    inputlist = input()
    for i in inputlist.split(','):
        result = i
        subjectscore.append(result)
    # 请在此添加代码，填入for循环遍历学生分数的代码
    # ********** Begin *********#
    for score in subjectscore:
        # ********** End **********#
        score = int(score)
        sum = sum + score
    print("第%d位同学的总分为:%d" % (student, sum))


# 第五关
List = []
member = input()
for i in member.split(','):
    result = i
    List.append(result)


# 请在此添加代码，将List转换为迭代器的代码
# ********** Begin *********#
class MyIterator:
    def __init__(self, mylist):
        self.mylist = mylist
        self.num = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num >= len(self.mylist):
            raise StopIteration
        return self.mylist[self.num]


# ********** End **********#
while True:
    try:
        # 请在此添加代码，用next()函数遍历IterList的代码
        # ********** Begin *********#
        obj1 = MyIterator(List)
        for i in range(len(List) + 1):
            num = next(obj1)
            # ********** End **********#
            result = int(num) * 2
            print(result)
    except StopIteration:
        break








