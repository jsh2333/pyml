#import MySQLdb
import pymysql
conn = pymysql.connect(
    user='root',
    passwd='pass',
    host='localhost',
    db='test',
    port=3306
)

cur = conn.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print ("Database version : %s " % data)



# cur.execute('DROP table items')
cur.execute('''
    create table items(
        item_id INTEGER PRIMARY KEY auto_increment,
        name text,
        price integer
    )
'''
)

data = [('banana', 300), ('mango', 600), ('apple', 200)]
for i in data:
    cur.execute("insert into items(name, price) values (%s, %s)", i)

cur.execute("select * from items")
for row in cur.fetchall():
    print(row)



conn.close()

