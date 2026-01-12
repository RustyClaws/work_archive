from bs4 import BeautifulSoup
import requests
import time
# import pandas as pd
import os

url = 'https://m.55123.cn/kjh/js7ws-history-120.htm'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')



target_tag = soup.find_all('span', class_="ball lred")
contents = []
for i in target_tag:
	contents.append(i.string)
#print(contents)
#	print(i.string)



# ===== 制作以时间为文件名的存储文件 =======

now_time = time.strftime('%Y-%m-%d')
filename = "raw" + str(now_time) + ".txt"

file_path = 'data/'
target = os.path.join(file_path, filename)

if not os.path.exists(target):
	f = open(target, "x")
else:
	pass

# ======= 获取最近120条 ========
n = 7

with open(target, "w", encoding='utf-8') as f1:
	for sep in [contents[i: i+n]  for i in range(0,len(contents), n)]:   #for里复合一个for
		#print(sep)
		f1.writelines(sep)
	f1.close()


	