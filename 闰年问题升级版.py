# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年月25日
"""
"""
题目要求：输入年月日，输出该日期是否是闰年，并且输出该日期是此年份的第几天
"""

class Leap_year:

    def __init__(self):
        self.big_month = [1,3,5,7,8,10,12]

    #获取天数并判断输入的数据是否合法
    def get_datatime(self):
        a = input("请输入合法的年月日，并且之间用‘-’隔开：")

        #判断是否有按照正确的年月日格式输入
        try:
            year,month,day = a.split("-")
        except ValueError:
            print("请输入正确的年月日格式！")
            return

        #判断输入的年月日是否越界
        if year.isdecimal() and month.isdecimal() and day.isdecimal():
            year = int(year)
            month = int(month)
            day = int(day)
            if month<=0 or month >= 13 :
                print("请输入正确的月份！")
                return
            else:
                if month == 2 and 1 <= day <= 29:
                    return year, month, day
                elif month in self.big_month and 1<= day <= 31:
                    return year, month, day
                elif 1 <= day <= 30:
                    return year, month, day
                else:
                    print("请输入正确的日！")
                    return
        else:
            print("请输入正确数字的年月日，输入的东西中可能包含非数字的东西！")
            return

    #判断是否为闰年
    def Judge(self,data):
        year, month, day = data
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            print("是闰年")
            return 1
        else:
            print("不是闰年")
            return 0

    #计算天数
    def count_day(self,data):
        year, month, day = data
        count = day
        for i in range(1,month + 1):
            if i == 2:
                count += 29
            elif i == 1:
                continue
            elif i in self.big_month:
                count += 31
            else:
                count +=30

        return count

    # 运行入口
    def run(self):
        while 1:
            message = self.get_datatime()
            if message:
                if self.Judge(message):
                    a = self.count_day(message)
                    print("该日期是此年份的第{}天".format(a))
                    break
                else:
                    print("啥时候是闰年就让你停下来！！！")

if __name__ == '__main__':
    c = Leap_year()
    c.run()

