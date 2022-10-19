# 初始化model模型到database
from db.User import User
from db.basemodel import _mdb

# create new table

tables = [User]
_mdb.drop_tables(tables)

_mdb.drop_tables(tables)
_mdb.create_tables(tables)
_mdb.commit()
