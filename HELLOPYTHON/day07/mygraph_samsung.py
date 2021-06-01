from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql


def getPrice(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    sql = """
    SELECT s_price FROM stock WHERE s_name = '{}'
    ORDER BY crawl_date
    """.format(s_name)
    curs.execute(sql)
    
    rows = curs.fetchall()
    
    for row in rows:
        ret.append(row[0])
    
    conn.close()
    return ret



if __name__ == '__main__':
    ret = getPrice("삼성전자")
    print(ret)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    z = np.array(ret)
    z = (z / ret[0]) * 100
    x = np.array([1,1,1,1,1,1,1,1,1,1])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    print(z)
    ax.plot3D(x, y, z, 'green')
    
    
    ret = getPrice("삼성전자우")
    print(ret)
    # z = np.array(ret)
    z = (np.array(ret) / ret[0]) * 100
    x = np.array([1,1,1,1,1,1,1,1,1,1])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    print(z)
    ax.plot3D(x, y, z, 'blue')
    
    
    ax.set_title('stock price comparing graph')
    plt.show()
    