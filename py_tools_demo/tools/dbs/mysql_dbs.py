import pymysql


class MysqlDbs(object):
    def __init__(self,host,port,user,password,database,**kwargs):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        return db

    def update_mysql(self, sql):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
        finally:
            print("更新成功")
            self.get_connection().close()

    def get_mysql(self, sql):
        try:
            cursor = self.get_connection().cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(e)
        finally:
            self.get_connection().close()


if __name__ == '__main__':
    mysql_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "masicro",
        "database": "masicro"
    }
    s = MysqlDbs(**mysql_config)
    # sql = "select * from zhiwang4 limit 1000"
    sql = "update zhiwang4 set is_download=null where id=1"
    data = s.update_mysql(sql)
    print(data)