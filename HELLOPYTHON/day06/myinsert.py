import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

curs = conn.cursor()

sql = "insert into hello(col01, col02, col03) values(4,'4','4')"
curs.execute(sql)
conn.commit()

conn.close()

