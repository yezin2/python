import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree


xml_file = 'D:\workspace_python\CRAWL\src\main\webapp\chicken.xml'
doc = ET.parse(xml_file)
#root 노드 가져오기
root = doc.getroot()

for item in root.iter("item"):
    print(item.findtext("title"), end=">>>>>")
    print(item.findtext("description"))
    
    
    