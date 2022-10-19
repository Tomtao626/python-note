#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: post_views.py
@time: 2020/12/11
@contact: tp320670258@gmail.com
@site: xxxx.gggg.net
@software: PyCharm 
"""
from pony.orm import db_session, commit, select
from models.Post import Post
from models.Comment import Comment
from models.Category import Category


# 插入数据
@db_session
def create_post(title, content):
    Post(title=title, content=content)


title = "测试标题"
content = "不晓得填些啥..."
create_post(title, content)

"""
1.所有对数据库的读写都要在 db_sesion 中进行,
2.除了通过 with 当作 context manager 使用,也可以作为装饰器，让 db_session 对整个函数中有效（并且 db_session 允许嵌套）
3.更新了数据记得 commit 提交. 
4.在db_session下，
    commit（）将自动完成，
    数据库会话缓存将被清除
    自动数据库连接将返回到池中
"""
# 除了省却commit步骤以外，db_session还能帮你在Exception时，自动回滚。
# 想更Pythonic一点的话，可以使用上下文管理器


# 修改数据
@db_session
def update_post(content):
    # get方法先获取一条
    post_one = Post.get(post_pk=1)
    post_one.content = content


content = "内容暂无"
update_post(content)


# 表关联操作

with db_session:
    p = Post.get(post_pk=1)
    Comment(content="你瞅啥", post=p)
    Comment(content="瞅你咋地", post=p)

    # 查看关联的数据
    print(p.comments)

# 之后就可以通过p.comments取到与之关联的评论。
# 那么再来试试多对多关系

with db_session:
    c1 = Category(name="tech")
    c2 = Category(name="blog")

    Post(title="第5篇文章", content="Hello world too", categories=[c1])
    Post(title="第6篇文章", content="Hello world 3", categories=[c1, c2])

    # 查看关联的数据
    print(Category["tech"].posts)  # 这个Category["tech"]等同于Category.get("tech")
    print(Post[6].categories)


# 删除
# 调用Entity实例的.delete()方法可以删掉这条数据。
# 如果需要把相关联的数据一并删掉，需要在定义model字段的时候加上cascade_delete = True的参数。

with db_session:
    Category["tech"].delete()


# 查询PonyORM的查询方式比较魔性，和别的ORM有较大区别，这里给个简单的例子看看样子。
# 用Entity对象上的select方法，传入lambda 表达式进行查询，查了id大于2并且内容包含"world"的条目。

with db_session:
    query = Post.select(lambda p: p.post_pk > 2 and "world" in p.content)
    print(list(query))  # 将query对象转为list，触发真正的查询获取数据

# 使用另一种方式用select函数，传入一个生成器表达式作为参数，查询了以"咋地"结尾的Comment。

with db_session:
    query = select(p.content for p in Comment if p.content.endswith("咋地"))
    print(query[:])  # 另一种转list的方式
# 使用SQL直接查询。

with db_session:
    query = Category.select_by_sql("SELECT * FROM category LIMIT 1")
    print(query[:])


