#!/usr/bin/env python
# coding:utf-8

from peewee import OperationalError, MySQLDatabase
from peewee import __exception_wrapper__
from .mysql import ReConnectMysqlDatabase
from output import conf


class RetryOperationalError(object):
	def execute_sql(self, sql, params=None, commit=True):
		try:
			cursor = super(RetryOperationalError, self).execute_sql(
				sql, params, commit)
		except OperationalError:
			if not self.is_closed():
				self.close()
			with __exception_wrapper__:
				cursor = self.cursor()
				cursor.execute(sql, params or ())
				if commit and not self.in_transaction():
					self.commit()
		return cursor


class RetryMySQLDatabase(RetryOperationalError, MySQLDatabase):
	pass


database = 'devt'
_mdb = RetryMySQLDatabase(database=database, **conf.read_conf(conf_type='mysql')[database])

#
# _mdb=ReConnectMysqlDatabase(database, **mysql_config["user_r"])


#
# from peewee import SqliteDatabase
# _mdb = SqliteDatabase("changshangtong.db")
