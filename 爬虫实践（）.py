# -*— coding:utf_8 -*-
"""
作者:程民华
日期:2022年01月08日
"""
import os
import requests
from bs4 import BeautifulSoup

#咳咳 运行后都说好
#重在学习里面的知识！

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fk = os.path.join(BASE_DIR, '4k')
if not os.path.isdir(fk):
    os.mkdir(fk)
for index in range(71, 101):  # 爬取前10页
    url = "https://pic.netbian.com/4kmeinv/index.html" if index == 1 else "https://pic.netbian.com/4kmeinv/index_{}.html".format(index)
    response = requests.get(url=url)
    bs = BeautifulSoup(response.text, "html.parser")   # bs用来解析html页面用的
    ul = bs.find(name='ul', attrs={"class": "clearfix"})
    a_list = ul.find_all(name='a')
    for a in a_list:
        a_url = "https://pic.netbian.com/" + a.get("href")
        a_response = requests.get(url=a_url)
        a_bs = BeautifulSoup(a_response.text, 'html.parser')
        img_url = "https://pic.netbian.com/" + a_bs.find(name="a", attrs={"id": "img"}).find('img').get('src')
        file_path = os.path.join(fk, img_url.rsplit('/', 1)[-1])
        with open(file_path, 'wb') as f:
            img_response = requests.get(url=img_url)
            f.write(img_response.content)
        print(img_url, 'download done .....')
    print('第{}页爬取完毕...'.format(index))

