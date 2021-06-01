import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

curs = conn.cursor()

sql = "DELETE FROM hello WHERE col01 = %s"
curs.execute(sql, 3)
conn.commit()

conn.close()

