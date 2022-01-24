# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年11月17日
"""
import random

print("游戏规则：生成一副扑克，然后用户按顺序抽牌，抽到数字则加上该数字的值，抽到'J''Q''K''小王''大王'则加上0.5分，若分数超过11，则爆掉，得0分，最后分数最高者获胜！")
begin = input("输入任意键将开始生成牌：")

# 生成牌
color_list = ["红桃", "黑桃", "方片", "梅花"]
specical_card = ['J', 'Q', 'K']
user_list = ["user1", "user2", "user3"]
num_list = []  # 相当于一个中转站，将列表转换为元组
all_card = []  # 储存所有的牌，牌库。
result = {}  # 储存最后所有玩家的分数

for num in range(1, 11):  # 这边是生成1-10的扑克
    for color in color_list:  # 嵌套循环，生成扑克
        num_list.append(color)  # 这一行和下一行是将循环到的元素加到中转列表中
        num_list.append(str(num))
        num_list_1 = tuple(num_list)  # 将中转列表转换为元组
        all_card.append(num_list_1)  # 将生成的该张牌放到牌库中
        num_list = []  # 将中转站归零

for card in specical_card:  # 思路和上面一样，这边是生成”J“”Q“”K“牌
    for color in color_list:
        num_list.append(color)
        num_list.append(card)
        num_list_1 = tuple(num_list)
        all_card.append(num_list_1)
        num_list = []

all_card.append(('大王', "红"), )  # 加入大小王。
all_card.append(('小王', "黑"), )
print(all_card)  # 输出所有的牌

for user in user_list:  # 让玩家一个个出来抽牌
    scord = 0  # 分数的起始,归零
    print("当前的玩家是{}".format(user))  # 输出现在的玩家是谁
    index = random.randint(0, len(all_card) - 1)  # 随机抽牌
    get_card = all_card.pop(index)
    if get_card[1].isdecimal():  # 判断抽出的牌是不是数字，是就直接加上，不是就加上0.5分
        scord += int(get_card[1])  # 将分数加起来
        print("当前抽到的牌是{}，当前的分数是{}".format(get_card, scord))  # 输出当前的结果
        print("当前剩的牌还有{}".format(all_card))  # 输出还剩多少牌
    else:
        scord += 0.5
        print("当前抽到的牌是{}，当前的分数是{}".format(get_card, scord))  # 输出当前的结果
        print("当前剩的牌还有{}".format(all_card))  # 输出还剩多少牌
    while True:  # 抽牌的主程序，以下所有的break都是跳出while循环，进入下一个玩家

        question = input("是否需要抽一张牌（Q/q放弃抽牌,回车键继续抽牌）：")  # 选择是抽牌还是退出
        if question.upper() == "Q":
            result[user] = scord  # 将玩家的分数储存起来
            break
        else:
            index = random.randint(0, len(all_card) - 1)  # 随机抽牌
            get_card = all_card.pop(index)
            if get_card[1].isdecimal():  # 判断抽出的牌是不是数字，是就直接加上，不是就加上0.5分
                scord += int(get_card[1])  # 将分数加起来
                print("当前抽到的牌是{}，当前的分数是{}".format(get_card, scord))  # 输出当前的结果
                print("当前剩的牌还有{}".format(all_card))  # 输出还剩多少牌
                if scord <= 11:
                    continue
                else:
                    print("{}当前的分数是{}，超过了11，爆了！".format(user, scord))  # 输出当前的结果
                    print("当前剩的牌还有{}".format(all_card))  # 输出还剩多少牌
                    scord = 0  # 爆了以后分数归零
                    result[user] = scord  # 将玩家的分数储存起来
                    break
            else:
                scord += 0.5
                print("当前抽到的牌是{}，当前的分数是{}".format(get_card, scord))  # 输出当前的结果
                print("当前剩的牌还有{}".format(all_card))  # 输出还剩多少牌
                if scord <= 11:  # 判断分数爆了没
                    continue  # 没爆就继续抽
                else:
                    print("{}当前的分数是{}，超过了11，爆了！".format(user, scord))  # 输出当前的结果
                    print("当前剩的牌还有{}".format(all_card))  # 输出还剩多少牌
                    scord = 0  # 爆了以后分数归零
                    result[user] = scord  # 将玩家的分数储存起来
                    break

print("游戏结束，分数的情况是{}".format(result))  # 输出最后的结果
