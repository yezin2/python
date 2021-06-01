import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

tuts = (
    ('3','3','3')
    )
curs = conn.cursor()

sql = "update hello set col01 = %s, col02 = %s, col03 = %s where col01 = 4"
curs.execute(sql, tuts)
conn.commit()

conn.close()