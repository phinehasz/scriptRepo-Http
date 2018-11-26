# coding=UTF-8
import mysql.connector

conn = mysql.connector.connect(user='root', password='****', database='**',host='***')
cursor = conn.cursor()
cursor.execute('select * from video where id<40000000 order by id desc limit 1')
values = cursor.fetchall()
print(values)
