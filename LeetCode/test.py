#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: test.py
@time: 2019/1/28 028 13:18
@desc:
'''
import pymysql
db = pymysql.connect('127.0.0.1','root','','hotel')
cur = db.cursor()
# cur.execute('SELECT * FROM hotel_manage_guest')
# data = cur.fetchall()
# data = pymysql.connect('127.0.0.1','root','','hotel').cursor().execute('select table_name from information_schema.tables')
# print(type(data))
print(type(cur))
print(().__class__.__bases__[0].__subclasses__())
print(().__class__.__bases__[0].__subclasses__()[-16].__init__())