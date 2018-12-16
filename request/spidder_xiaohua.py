#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
#from gevent import monkey
import gevent
import datetime

#monkey.patch_all()
def my_download(url):
    result=requests.get(url)
    mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
    video=requests.get(mp4_url)
    print(mp4_url)
    info = '{time}.mp4'.format(time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    with open(info,'wb') as f:
        f.write(video.content)


video_list = []
respose=requests.get('http://www.xiaohuar.com/v/')
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
print(respose.text)  #返回文本内容
urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
#print(urls)
#print(len(urls))
for i in range (0,len(urls)):
    video_list.append( gevent.spawn(my_download,urls[i]))

print(len(video_list))
gevent.joinall(video_list)

url=urls[5]
print( url)
#result=requests.get(url)
#mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

#video=requests.get(mp4_url)

#with open('D:\\a.mp4','wb') as f:
#   f.write(video.content)

