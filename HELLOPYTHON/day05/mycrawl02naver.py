import requests
from bs4 import BeautifulSoup

url = "http://localhost/CRAWL/crawl.html"

response = requests.get(url)

if(response.status_code == 200):
    html = response.text
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    res = ""
    i = 1
    for tag in soup.select('td'):
        # print(tag.text)
        res = res + tag.text
        if((i%2) == 1):
            res = res + " : "
        elif((i%2) == 0):
            res = res + "\n"
        # print("@@@")
        i = i+1
    print(res)
    
    # tds = soup.select("td")
    # for i,td in enumerate(tds):
    #     print(td.get_text())
    #     # if i > 1:
    #     #     print(td.get_text())
else : 
    print(response.status_code)