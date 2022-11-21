import MySQLdb
import numpy as np
import peewee
from peewee import *


def test_pymysql():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='your_username',
        passwd='your_password',
        db='mysql'
    )

    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE price (
                timestamp TIMESTAMP NOT NULL,
                BTCUSD FLOAT(8,2),
                PRIMARY KEY (timestamp)
            );
        ''')
    cur.execute('''
            INSERT INTO price VALUES(
                "2029-07-14 14:12:17",
                11234.56
            );
        ''')

    conn.commit()
    conn.close()


db = MySQLDatabase('mysql', user='your_username', passwd='your_password')


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    Price.create_table()
    price = Price(timestamp='2029-06-07 13:17:18', BTCUSD='12345.67')
    price.save()


def test_pymysql_new():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='your_username',
        passwd='your_password',
        db='mysql'
    )

    cur = conn.cursor()
    cur.execute('''
            SELECT
              BTCUSD
            FROM
              price
            WHERE
              timestamp > now() - interval 60 minute
    ''')

    BTCUSD = np.array(cur.fetchall())
    print(BTCUSD.max(), BTCUSD.min())

    conn.close()


if __name__ == '__main__':
    test_pymysql()
    test_peewee()
    test_pymysql_new()