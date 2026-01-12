import pandas as pd
import re

datafile = ''												# 如果有数据文件，填在这里
def replace_sh1():
	sheet1 = pd.read_excel(filename, sheet_name = 0)		# 打开表
	with open(datafile) as f:
		