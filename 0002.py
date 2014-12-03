#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'vovo'

import uuid
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="1", db="showmethecode", charset="utf8")
cursor = conn.cursor()

sql = "insert into app_users(api_key) values('%s')"


for a in xrange(0, 200):
    a = uuid.uuid1()
    exesql = sql % a
    try:
        cursor.execute(exesql)
        conn.commit()
    except:
        conn.rollback()
        print "error"

cursor.close()
conn.close()




