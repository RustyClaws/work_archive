import re
import pandas as pd

filename =  "raw.xlsm"  									 # 文件名在这里修改. 要修改的文件和本文件在同一目录只需要填文件名，不同目录要输入完整路径


def replacement():         									# 修改文件中所有B、C列中，要求被修改的部分：将该部分替换为"{}"
	sheet1 = pd.read_excel(filename, sheet_name = 0)
	sheet2 = pd.read_excel(filename, sheet_name = 1)
	sheet3 = pd.read_excel(filename, sheet_name = 2)
	sheet4 = pd.read_excel(filename, sheet_name = 3)		# 读取4张表 

	print("=== 读取成功，任务进行中，请稍等 ===")
	with open('regexp.txt', "r") as f:						# 读取文件内容
		regexp = f.readlines()		   
		for line in regexp:
			if line.find('-') != -1:
				line = line.replace('-','')
				line = "-" + line
			reg = line.replace('\n', '')					# 调整regexp的表达式
			reg = re.compile(reg)							# 用complie预编译
			#print(reg)

			sheet1['標題'].replace(reg, '<>', regex = True, inplace = True)
			sheet1['說明'].replace(reg, '<>', regex = True, inplace = True)
			sheet2['標題'].replace(reg, '<>', regex = True, inplace = True)
			sheet2['說明'].replace(reg, '<>', regex = True, inplace = True)
			sheet3['標題'].replace(reg, '<>', regex = True, inplace = True)
			sheet3['說明'].replace(reg, '<>', regex = True, inplace = True)
			sheet4['標題'].replace(reg, '<>', regex = True, inplace = True)
			sheet4['說明'].replace(reg, '<>', regex = True, inplace = True)

		sheet1.to_excel('files/1.xlsm', index = False)
		sheet2.to_excel('files/2.xlsm', index = False)
		sheet3.to_excel('files/3.xlsm', index = False)
		sheet4.to_excel('files/4.xlsm', index = False)


#		输出四个文件，然后合并成一个，四个文件分别是四个工作表, 名称1、2、3、4分别对应原表中：sheet1 sheet1(2) sheet1(3) sheet1(4)
	
	print("=== 替换已全部完成完成！ ===")

	



if __name__ == '__main__':
	replacement()