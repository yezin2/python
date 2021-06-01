import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insertChicken(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "insert into chicken(title, link, description, bloggername, bloggerlink, postdate) values(%s,%s,%s,%s,%s,%s)"
    cnt = curs.executemany(sql,tuts)
    
    conn.commit()
    conn.close()
    return cnt
    
client_id = "mgtDMqVtMV8yZtQDwjFT"
client_secret = "LYTDxl9pBy"
encText = urllib.parse.quote("치킨")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()

    html = response_body.decode("utf-8")
    soup = BeautifulSoup(html, "xml")
    
    tuts = []
    item = soup.select("item")
    for i,item in enumerate(item):
        title = item.title.text
        link = item.link.text
        description = item.description.text
        bloggername = item.bloggername.text
        bloggerlink = item.bloggerlink.text
        postdate = item.postdate.text
        tuts.append((title, link, description, bloggername, bloggerlink, postdate))
        
    cnt = insertChicken(tuts)
    print("cnt : ", cnt)
        
else:
    print("Error Code:" + rescode)




