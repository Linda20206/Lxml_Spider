
# coding: utf-8

# In[36]:


import requests
import lxml
import time
from lxml import etree


# In[37]:


def Get_Html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36 Edg/86.0.622.63'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        print("请求失败")


# In[38]:


def Get_Info(html):
    html = etree.HTML(html)
    infos = html.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('./td[2]/div[1]/a/text()')[0]
        brief = info.xpath('./td[2]/p[1]/text()')[0]
        score = info.xpath('./td[2]/div[2]/span[2]/text()')[0]
        number = info.xpath('./td[2]/div[2]/span[3]/text()')[0]
        data = {'name':name.replace('\n','').replace(' ',''),
               'brief':brief,
               'score':score,
               'number':number.replace('\n','').replace(' ','')}
        print(data)


# In[39]:


urls = ["https://book.douban.com/top250?start={}".format(i) for i in range(0,226,25)]
for url in urls:
    html = Get_Html(url)
    Get_Info(html)
    time.sleep(1)

