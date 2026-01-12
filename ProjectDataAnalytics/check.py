import pandas as pd

f = open("data/raw2024-04-15.txt", "rt")
raw_data = f.read()
tmp = []
for i in range(int(len(raw_data) / 7)):
	# print(raw_data[7*i: 7*i+7])         # seperate numlist into 7 digits per line
	tmp.append(raw_data[7*i : 7*i+7])
sorted_data = tmp[::-1]                   # reversed datas, with the oldest on the top, easily append new data to the new file
c = open("data/datastr.txt", "w")                 # create a new file to save seperated data lines. when it is needed to add new data, open datastr.txt

for nums in sorted_data:
	c.write(nums+'\n')
c.close()
