import pandas as pd
import time
#import re

def rule_match():
	start = time.perf_counter()
	# ==== 计算时间 ====

	test_df = pd.read_excel('test.xlsx')
	rules_df = pd.read_excel('規則.xlsx')
	print("=== 读取成功，开始匹配 ===")
	# 如果不存在，分别创建两列
	if '拍賣類別' not in test_df.columns:
		test_df['拍賣類別'] = ""
	if '拍賣類別名稱' not in test_df.columns:
		test_df['拍賣類別名稱'] = ""

	new_clos = pd.DataFrame(columns = ['分類編號', '分類名稱'])
	
	# 逐行匹配
	for lines, rule in rules_df.iterrows():
		rule_keyword = rule['規則'].split(',')
		rule_category_id = rule['分類編號']
		rule_category_name = rule['分類名稱']

		# ==== 用for循环匹配，代价：嵌套循环导致时间变长 === 
		for keys in rule_keyword:
			flag = 1
			is_match = test_df['標題'].str.contains(keys,regex=False, na=False)
			if is_match is True:
				flag *= 1
			else:
				flag *= 0
			# 在每一个规则里面找，但凡有一个不符合，flag=0,即不符合
		if flag == 1:
			new_clos = new_clos._append({'分類編號':rule_category_id,'分類名稱':rule_category_name}, ignore_index = True)
		# ===  === ===


		# 防止只有一个元素报错
			#if len(rule_keyword) > 1:
		#keyword_pattern = '\|'.join(rule_keyword)
		#keyword_pattern = '|'.join(map(re.escape, rule_keyword))

		
		#keyword_pattern = re.compile(keyword_pattern)
		# 正则预编译
		#matches = test_df['標題'].str.contains(keyword_pattern, regex=True, na=False)
		# 确保每个都匹配上
		#new_clos = new_clos._append({'分類編號':rule_category_id,'分類名稱':rule_category_name}, ignore_index = True)
		
	

	print("匹配和制表已完成，正在输出新文件")
	output_file = 'updated_test_new.xlsx'
	test_df.to_excel(output_file, index = False)
	print("=== 文件已保存 ===")
	# ==== 计算时间 ====
	end = time.perf_counter()
	print('time consumed: %s s'%(end-start))
	

if __name__ == '__main__':
	rule_match()
	