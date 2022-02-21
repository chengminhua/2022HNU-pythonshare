~~~sql
create database blogsystem;
~~~

~~~sql
--个人信息
create table message(
id int not null auto_increment primary key,
name varchar(16) not null,
showname varchar(16) not null,
phone char(11) not null,
email varchar(24) not null,
passwd varchar(64) not null,
unique un_name (name),
unique un_showname (showname),
index ix_name_passwd (name,passwd)
)default charset=utf8;
~~~

~~~sql
--博客
create table blog_content(
id int not null auto_increment primary key,
name varchar(16) not null,
content text not null,
time datetime not null,
readtimes int default 0,
commenttimes int default 0,
up_num int default 0,
down_num int default 0,
constraint fk_blogcontent_message foreign key (name) references message(showname)
)default charset=utf8;
~~~

~~~sql
--评论
create table comment_content(
id int not null auto_increment primary key,
content_id int not null,
name varchar(16) not null,
time datetime not null,
content varchar(128) not null,
constraint fk_commentmessage_message foreign key (name) references message(showname),
constraint fk_commentmessage_blogcontent foreign key (content_id) references blog_content(id)
)default charset=utf8;
~~~

~~~sql
--点赞和点踩
create table up_dowm(
id int not null auto_increment primary key,
name varchar(16) not null,
content_id int not null,
time datetime not null,
choice tinyint not null,
constraint fk_updown_message foreign key (name) references message(showname),
constraint fk_updown_blogcontent foreign key (content_id) references blog_content(id),
unique un_name_contentid (name,content_id)
)default charset=utf8;
~~~

