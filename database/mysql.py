#coding:utf-8

mport MySQLdb

myDB = MySQLdb.connect(host="127.0.0.1", port=3306)
cHandler = myDB.cursor()

cHandler.execute("SHOW DATABASES")
results = cHandler.fetchall()

for item in results:
    print item[0]

cHandler.execute("SELECT DATABASE()")
results = cHandler.fetchall()
k
for item in results:
    print item[0]

cHandler.execute("USE schedule")
cHandler.execute("SELECT DATABASE()")
results = cHandler.fetchall()

for item in results:
    print item[0]

myDB.close()
