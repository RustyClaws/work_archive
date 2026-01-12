# add new data: 
# 1- read the last line in datastr.txt
# 2- get the newest data, if not = last-line, append to datastr; else stop
# 3- save the datas.

from bs4 import BeautifulSoup
import requests
import re

fname = 'data/datastr.txt'
with open(fname, 'r', encoding = 'UTF-8') as f:
	lines = f.readlines()
	last_line = lines[-1]

print("the last data is:", last_line)                                       # the last line in local database.


# ======= get new datas from website =============

url = 'https://www.js-lottery.com/Chart/sevenFenBu'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


table = soup.find('table', class_= "table table-bordered")
new_data = []                                                                # new datas to get
# rows = table.find_all('tr')
for i in range(4,53)[:: -1]:
	data = table.find_all('tr')[i].find_all('td')[1].text
	data2 = ''.join(data.split())
	# print(data2)
	new_data.append(data2)

print(new_data)

