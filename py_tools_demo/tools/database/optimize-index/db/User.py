#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/4 6:02 下午
# @Author : admin
# @Software: PyCharm
# @File: User.py


from db.basemodel import BaseModel
from peewee import CharField, IntegerField, BooleanField


class User(BaseModel):
    """
    extra_user
    """
    # id = IntegerField(default=0, verbose_name='id', help_text='id', primary_key=True)
    user_name = CharField(max_length=128, default='', verbose_name='username', help_text='username', index=True)
    age = IntegerField(default=0, verbose_name='age', help_text='age')
    address = CharField(max_length=128, default='', verbose_name='address', help_text='address')

    class Meta:
        table_name = 'user'
        verbose_name = '用户'

    def _to_dict(self):
        keys = ['id', 'username', 'age', 'address']
        return self.to_dict(keys)
