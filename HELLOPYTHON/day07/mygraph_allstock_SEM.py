from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from random import *

conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

def getNames():
    ret = []
    sql = "SELECT s_code FROM stock GROUP BY s_name"
    curs.execute(sql)
    
    rows = curs.fetchall()
    
    for row in rows:
        ret.append(row[0])
    
    return np.array(ret)

def getPrice(s_code):
    ret = []
    sql = """SELECT s_price FROM stock WHERE s_code = '{}' ORDER BY crawl_date""".format(s_code)
    curs.execute(sql)
    
    rows = curs.fetchall()
    
    for row in rows:
        ret.append(row[0])
    
    return np.array(ret)

def getRGB():
    r = random()
    g = random()
    b = random()
    a = random()
    color = (r,g,b,a)
    return color

arr_name = getNames()
print(arr_name)

arrz = []
arrz.append(getPrice(arr_name[0]))
arrz.append(getPrice(arr_name[1]))

arr_per_z = []
imsi0 = (arrz[0]/arrz[0][0])*100
arr_per_z.append(imsi0)
imsi1 = (arrz[1]/arrz[1][0])*100
arr_per_z.append(imsi1)

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.array([1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9])

color = getRGB()
ax.plot3D(x+0, y, arr_per_z[0])

color = getRGB()
ax.plot3D(x+1, y, arr_per_z[1])

ax.set_title('stock price comparing graph')
plt.show()
    
conn.close()