from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from random import *

conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

def getCode():
    ret = []
    sql = "SELECT s_code FROM stock GROUP BY s_code"
    curs.execute(sql)
    
    rows = curs.fetchall()
    
    for row in rows:
        ret.append(row[0])
    
    return ret

def getPrice(s_code):
    ret = []
    sql = """SELECT s_price FROM stock WHERE s_code = '{}' ORDER BY crawl_date""".format(s_code)
    curs.execute(sql)
    
    rows = curs.fetchall()
    
    for row in rows:
        ret.append(row[0])
    
    return ret

def getRGB():
    r = random()
    g = random()
    b = random()
    a = random()
    color = (r,g,b,a)
    return color


getCodes = getCode()
print(getCodes)
colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple", "pink"]
fig = plt.figure()
ax = plt.axes(projection='3d')
for i,code in enumerate(getCodes):
    get_prices = getPrice(code)
    print(get_prices)
    z = np.array(get_prices)
    z = (z / get_prices[0]) * 100
    x = np.array([1,1,1,1,1,1,1,1,1,1])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    print(z)
    
    color = getRGB()
    ax.plot3D(x+i, y, z, c=color)
    # ret = getPrice("삼성전자")
    # print(ret)
    #
    #
    # ret = getPrice("삼성전자우")
    # print(ret)
    # # z = np.array(ret)
    # z = (np.array(ret) / ret[0]) * 100
    # x = np.array([1,1,1,1,1,1,1,1,1,1])
    # y = np.array([0,1,2,3,4,5,6,7,8,9])
    # print(z)
    # ax.plot3D(x, y, z, 'blue')
    #
    #
ax.set_title('stock price comparing graph')
plt.show()
    
conn.close()