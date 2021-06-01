import requests
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime
import time

def insertStock(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "insert into stock(s_code, s_name, s_price, crawl_date) values(%s,%s,%s,%s)"
    cnt = curs.executemany(sql,tuts)
    
    conn.commit()
    conn.close()
    return cnt

for i in range(10):
    url = "http://vip.mk.co.kr/newSt/rate/item_all.php"
    
    response = requests.get(url)
    
    if(response.status_code == 200):
        html = response.text
        # print(html)
        tuts = []
        soup = BeautifulSoup(response.content.decode("euc-kr", "replace"), "html.parser")
        
        now = datetime.now()
        crawl_date = now.strftime('%Y%m%d.%H%M')
        
        for i,tag in enumerate(soup.select('.st2')):
            s_code = tag.select_one('a').attrs['title']
            s_name = tag.get_text();
            s_price = tag.find_next_sibling('td').get_text().replace(",","")
            # time = ('2021.' + soup.select_one('.t_11_black').get_text()).replace(" ", ",").replace(".","").replace(":","")
            # crawl_date = time.replace(",",".")
            tuts.append((s_code, s_name, s_price, crawl_date))
            # print(tuts)
        cnt = insertStock(tuts)
        print("cnt : ", cnt)
        
        # tds = soup.select("td")
        # for i,td in enumerate(tds):
        #     print(td.get_text())
        #     # if i > 1:
        #     #     print(td.get_text())
    else : 
        print(response.status_code)
    time.sleep(60)