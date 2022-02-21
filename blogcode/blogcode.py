import pymysql
import hashlib
from datetime import datetime
import re


class MyBlogSystem:
    username = ""

    def __init__(self, conn):
        self.conn = conn

    # 展示可用的方法
    @staticmethod
    def show_function():
        for key, value in function_dic.items():
            print("{}.{}".format(key, value))

    # 密码加密储存
    @staticmethod
    def passwd_hash(passwd):
        hash_object = hashlib.md5()
        hash_object.update(passwd.encode("utf-8"))
        hash_result = hash_object.hexdigest()
        return hash_result

    # 用来验证用户注册的各种信息是否合法，提前一步验证，省的插不进mysql中
    @staticmethod
    def verify_message(phone, email, passwd, name, showname):

        # 验证输入的信息有没有空的
        if not all([phone, email, passwd, name, showname]):
            return 0

        # 判断邮箱格式对不对
        str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if not re.match(str, email):
            print("邮箱格式不对")
            return

            # 验证手机号是不是11位
            pattern = re.compile(r"1[356789]\d{9}")
            result = pattern.findall(phone)
            if not result:
                print("手机号有问题")
                return 0

        # 判断密码的强度怎么样
        patterns = re.compile(r"[a-zA-Z](?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}")
        result = patterns.findall(passwd)
        if not result:
            print("密码应该有的格式：以字母开头，必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-16之间  （请修改）")

        # 判断name那些的有没有太长
        if len(name) <= 16 and len(showname) <= 16:
            pass
        else:
            print("登录名和昵称都不能长于16个字符，请修改！")
            return 0

        return 1

    # 注册函数
    def register(self, cursor):
        name = input("输入登录名：")
        showname = input("输入用于展示的昵称：")
        email = input("输入邮箱：")
        phone = input("输入11位手机号：")
        passwd = input("输入密码：")

        if not self.verify_message(phone, email, passwd, name, showname):
            print("请严格按照上面规定的格式输入，自己检查一下有没有输错的地方！")
        else:
            passwd = self.passwd_hash(passwd)
            try:
                cursor.execute("insert into message(name,showname,phone,email,passwd) values(%s,%s,%s,%s,%s)",
                               [name, showname, phone, email, passwd])
                conn.commit()
                print("注册成功！\n")
            except pymysql.err.IntegrityError:
                print("注册失败，登录名或昵称已存在")

    # 登录函数
    def log_in(self, cursor):
        name = input("请输入登录名：")
        passwd = input("请输入密码：")
        passwd = self.passwd_hash(passwd)

        cursor.execute("select showname from message where name=%s and passwd=%s",
                       [name, passwd])
        result = cursor.fetchone()

        if not result:
            print("登录名或密码错误，")
        else:
            MyBlogSystem.username = result[0]
            print("登录成功")

    # 登出函数
    def log_out(self, cursor):
        if not MyBlogSystem.username:
            print("请先登录！")
        else:
            MyBlogSystem.username = ""
            print("退出成功！")

    # 评论功能
    def todo_comments(self, cursor, id):
        print("\n突然有不想评论了请输q/Q")
        while 1:
            content = input("请输入你的评论：")
            if content.upper().strip() == 'Q':
                return

            if content:
                cursor.execute("insert into comment_content(content_id,name,time,content) values(%s,%s,%s,%s)",
                               [id, MyBlogSystem.username, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                content])
                self.conn.commit()
                cursor.execute(
                    "update blog_content set commenttimes = commenttimes+1 where id=%s", [id])
                self.conn.commit()
                print("继续浏览博客")
                return
            else:
                print("你倒是输点东西啊")

    # 点赞点踩的功能
    def up_or_down(self, cursor, choice, id):
        try:
            cursor.execute("insert into up_dowm(name,content_id,time,choice) values(%s,%s,%s,%s)",
                           [MyBlogSystem.username, id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            choice])
            self.conn.commit()
            if choice == '1':
                cursor.execute(
                    "update blog_content set up_num = up_num+1 where id=%s", [id])
                self.conn.commit()
                print("点赞成功！")
            else:
                cursor.execute(
                    "update blog_content set down_num = down_num+1 where id=%s", [id])
                self.conn.commit()
                print("点踩成功！")
        except pymysql.err.IntegrityError:
            print("您已经赞或踩过啦！！！")

    # 浏览博客详情的函数
    def skip_more_blog(self, cursor, title):
        # 确保是登录的用户可以看！！
        if not MyBlogSystem.username:
            print("想看详细内容请先登录哦")
            return

        # 增加当前博客的播放量
        cursor.execute(
            "update blog_content set readtimes = readtimes+1 where content_name=%s", [title])
        self.conn.commit()

        # 获取数据
        cursor.execute(
            "select id,name,content,time,up_num,down_num,content_name from blog_content where content_name=%s", [title])
        result = cursor.fetchone()
        id, name, content, time, up_num, down_num, content_name = result

        # 展示实际的内容
        print("""标题：{}
        正文：
        -----------
        {}
        -----------
        作者：{}
        上传时间：{}
        点赞数：{}
        点踩数：{}
        """.format(content_name, content, name, time, up_num, down_num))
        # 展示评论
        cursor.execute(
            "select comment_content.name,comment_content.time,comment_content.content from comment_content where comment_content.content_id=%s",
            [id])
        result = cursor.fetchall()

        print("评论：")
        for i in result:
            name, time, content = i
            print("""{} {}
            -----------------------
            {}
            -----------------------
            -----------------------
            """.format(time, name, content))

        # 评论，点赞or点踩
        print("\n\n退出直接输入q/Q")
        print("点赞请输1，点踩请输0，评论请输入‘pl’")
        while 1:
            order = input(">>>")
            if order.upper().strip() == 'Q':
                print("继续浏览博客")
                return

            if order == '1' or order == '0':
                self.up_or_down(cursor, order, id)
            elif order == "pl":
                self.todo_comments(cursor, id)
                break
            else:
                print("请输入正确的指令")

    # 发布博客
    def publish_blog(self, cursor):
        # 验证用户是否登录
        if not MyBlogSystem.username:
            print("请先登录")
            return

        while 1:
            content_title = input("输入你的博客标题：")
            content = input("输入博客内容：")
            if content_title and content:
                cursor.execute("insert into blog_content(name, content, time, content_name) values(%s,%s, %s, %s)",
                               [MyBlogSystem.username, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                content_title])
                self.conn.commit()
                print("发布成功！")
                return
            else:
                print("你确定在博客里面写东西了？")

    # 浏览博客大纲的函数
    def skip_blog(self, cursor):
        print("使用说明：")
        print("输入q/Q可退出看博客")
        print("直接复制博客的标题然后直接输入可直达博客的详细页！\n")
        while 1:

            cursor.execute('select * from blog_content')
            result = cursor.fetchall()
            blog_len = len(result)

            # 建立一个title库，省的后面麻烦
            title_list = []
            for i in range(int(blog_len)):
                title = result[i][-1]
                title_list.append(title)

            print("共有{}篇博客，一页展示10个博客，输入页码来读取相应的博客！".format(blog_len))

            order = input(">>>")
            if order.upper().strip() == "Q":
                break

            if order.isdecimal():
                order = int(order)
                a = int(blog_len) // 10
                b = int(blog_len) % 10
                if 0 < order <= a:
                    for i in range((order - 1) * 10, order * 10):
                        content = result[i]
                        content_name = content[-1]
                        name = content[1]
                        time = content[3]
                        readtimes = content[4]
                        committimes = content[5]
                        up_num = content[-3]
                        print("标题：{}     作者：{} 上传时间：{} 阅读数：{} 评论数：{} 点赞数：{}".format(content_name, name, time, readtimes,
                                                                                    committimes, up_num))
                elif 0 < (order - 1) * 10 <= a * 10 + b:
                    for i in range(a * 10, a * 10 + b):
                        content = result[i]
                        content_name = content[-1]
                        name = content[1]
                        time = content[3]
                        readtimes = content[4]
                        committimes = content[5]
                        up_num = content[-3]
                        print("标题：{}     作者：{} 上传时间：{} 阅读数：{} 评论数：{} 点赞数：{}".format(content_name, name, time, readtimes,
                                                                                    committimes, up_num))
                else:
                    print("页码范围输入的有问题，检查一下！")
            elif order in title_list:
                self.skip_more_blog(cursor, order)
            else:
                print("输入有误，请检查一下")

    # 入口函数
    def handle(self):
        # 先进入指定的数据库,初始化一些东西
        cursor = self.conn.cursor()
        cursor.execute("use blogsystem")
        print("输入功能前面的数字可使用功能！")
        print("输入（q/Q）可退出！")

        # 进入循环，接受指令
        while 1:
            self.show_function()
            order = input(">>>")
            if order.upper().strip() == 'Q':
                cursor.close()
                self.conn.close()
                print("欢迎下次再来")
                break
            else:
                if not order.strip():
                    print("请检查输入的方法有没有输错！")
                    continue

                if hasattr(self, function_dic.get(order.strip(), '0')):
                    getattr(self, function_dic.get(order.strip()))(cursor)
                else:
                    print("请检查输入的方法有没有输错！")


if __name__ == '__main__':
    # 维护一个功能池
    function_dic = {
        '1': "register",
        '2': "log_in",
        '3': "log_out",
        '4': "skip_blog",
        '5': "publish_blog",
    }

    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", charset="utf8")
    blog = MyBlogSystem(conn)
    blog.handle()
