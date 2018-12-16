import re
import requests

respose=requests.get('http://www.sihaidy.com')
#print(respose.status_code)# 响应的状态码
#print(respose.content)  #返回字节信息
#print(respose.text)  #返回文本内容
urls=re.findall(r'href="(.*?)">电影|电视剧',respose.text,re.S)
print(urls)
url=urls[0]
result=requests.get(url)
mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
print(mp4_url)
video=requests.get(mp4_url)

with open('D:\\a.mp4','wb') as f:
    f.write(video.content)
