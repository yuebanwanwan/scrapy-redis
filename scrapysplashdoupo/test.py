import scrapy
import requests
from lxml import etree
import re
base_urls = 'https://www.zhihu.com/people/excited-vczh/followers'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
response = requests.get(base_urls,headers = headers)
html = etree.HTML(response.text)

if response.status_code == 200:
    print('111')
    html = etree.HTML(response.text)
    #html.xpath()返回的是一个节点类型组成的list
    fllowers = html.xpath('//strong[@class="NumberBoard-itemValue"]//text()')
    print(type(fllowers))
    reallyf = str(fllowers[1])
    r2 = re.sub("\D","",reallyf)
    r3 = int(r2)




