# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2021年11月23日
"""

suci = [
    '水龙吟（似花还似非花）',
    '满庭芳（归去来兮）',
    '满庭芳（三十三年）',
    '水调歌头（落日绣帘卷）',
    '水调歌头（明月几时有）',
    '水调歌头（昵昵儿女语）',
    '满江红（江汉西来）',
    '念奴娇（赤壁怀古）',
    '沁园春（孤馆灯青）',
    '一丛花（今年春浅腊侵年）',
    '木兰花令（霜馀已失长淮阔）',
    '西江月（世事一场大梦）',
    '西江月（玉骨那愁瘴雾）',
    '西江月（照野弥弥浅浪）',
    '西江月（三过平山堂下）',
    '临江仙（忘却成都来十载）',
    '临江仙（夜饮东坡醒复醉）',
    '鹧鸪天（林断山明竹隐墙）',
    '少年游（去年相送）',
    '定风波（莫听穿林打叶声）',
    '定风波（好睡慵开莫厌迟）',
    '定风波（常羡人间琢玉郎）',
    '南乡子（晚景落琼杯）',
    '南乡子（寒雀满疏篱）',
    '南乡子（霜降水痕收）',
    '南乡子（回首乱山横）',
    '南歌子（雨暗初疑夜）',
    '鹊桥仙（缑山仙子）',
    '望江南（春未老）',
    '卜算子（缺月挂疏桐）',
    '昭君怨（谁作桓伊三弄）',
    '贺新郎（乳燕飞华屋）',
    '洞仙歌（冰肌玉骨）',
    '八声甘州（有情风万里卷潮来）',
    '江城子（凤凰山下雨初晴）',
    '江城子（密州出猎）',
    '江城子（乙卯正月二十日夜记梦）',
    '蝶恋花（花褪残红青杏小）',
    '蝶恋花（簌簌无风花自祥）',
    '蝶恋花（灯火钱塘三五夜）',
    '永遇乐（长忆别时）',
    '永遇乐（明月如霜）',
    '浣溪沙（山下兰芽短浸溪）',
    '浣溪沙（旋抹红妆看使君）',
    '浣溪沙（簌簌衣巾落枣花）',
    '浣溪沙（道字娇讹苦未成）',
    '沁园春（情若连环）',
    '行香子（清夜无尘）',
    '行香子（一叶舟轻）',
    '虞美人（湖山信是东南美）',
    '虞美人（波声拍枕长淮晓）',
    '河满子（见说岷峨凄怆）',
    '醉落魄（轻云微月）']

# cpname = input("输入要查询的词牌名:")  # 输入要查询的词牌名
# cp_dict = {}  # 保存苏轼词信息的字典
# ########## 补充代码开始 ##########
# #基本思路
# #1：将词牌分出来，并加入到cp_dict中
# for i in suci:
#     list_cipai = i.replace("）","").split("（")
#
#     # print(list_cipai)
#     if list_cipai[0] in cp_dict:
#         name = list_cipai[0]
#         # print(name)
#         num = cp_dict.get(list_cipai[0])+1
#         # print(num)
#         cp_dict.update({name:num})
#     else :
#         cp_dict[list_cipai[0]] = 1
#         # print(cp_dict)
# #2：在字典的值的位置表示该词牌的数量
# #3：完成上述操作后，尝试将键的位置换成列表并将每个词牌对应的诗句加入
#
# ########## 补充代码结束 ##########
# print('{}首苏轼词中有词牌{}个'.format(len(suci), len(cp_dict)))
# print('词牌“{}”共{}首'.format(cpname, cp_dict[cpname]))


#高级点，可以显示词牌对应的诗句
cpname = input("输入要查询的词牌名:")  # 输入要查询的词牌名
cp_dict = {}  # 保存苏轼词信息的字典
########## 补充代码开始 ##########
# 基本思路
# 1：将词牌分出来，并加入到cp_dict中
for i in suci:
    list_cipai = i.replace("）", "").split("（")

    # print(list_cipai)
    if list_cipai[0] in cp_dict:
        name = list_cipai[0]
        # print(name)
        cp_dict.get(list_cipai[0]).append(list_cipai[1])
        # print(num)
        cp_dict.update({name: cp_dict.get(list_cipai[0])})
    else:
        data = []
        data.append(list_cipai[1])
        # print(list_cipai[1],type(list_cipai[1]))
        # print(data)
        cp_dict[list_cipai[0]] = data
        # print(cp_dict)
# 2：在字典的值的位置表示该词牌的数量
# 3：完成上述操作后，尝试将键的位置换成列表并将每个词牌对应的诗句加入

########## 补充代码结束 ##########
print('{}首苏轼词中有词牌{}个'.format(len(suci), len(cp_dict)))
print('词牌“{}”共{}首'.format(cpname, len(cp_dict.get(cpname))))
print("他们分别是:")
for n in cp_dict.get(cpname):
    print(n)


