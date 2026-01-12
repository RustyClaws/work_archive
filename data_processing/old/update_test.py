import pandas as pd
import time

start = time.perf_counter()

print("Loading Excel files...")

# 加载提供的Excel文件
test_df = pd.read_excel('test.xlsx')
rules_df = pd.read_excel('規則.xlsx')

print("Excel files loaded.")

# 确保 '拍賣類別' 和 '拍賣類別名稱' 列存在于test DataFrame中，并设置为字符串类型
if '拍賣類別' not in test_df.columns:
    test_df['拍賣類別'] = ""
if '拍賣類別名稱' not in test_df.columns:
    test_df['拍賣類別名稱'] = ""

test_df['拍賣類別'] = test_df['拍賣類別'].astype(str)                   #这里有一个astype
test_df['拍賣類別名稱'] = test_df['拍賣類別名稱'].astype(str)

print("Starting rule matching...")

# 创建一个用于存储匹配结果的DataFrame
results = pd.DataFrame(columns=['分類編號', '分類名稱'])

# 处理规则匹配
for index, rule in rules_df.iterrows():
    rule_keywords = rule['規則'].split(',')
    rule_category_id = rule['分類編號']
    rule_category_name = rule['分類名稱']
    
    # 矢量化匹配规则
    matches = test_df['標題'].apply(lambda x: all(keyword in x for keyword in rule_keywords))
    
    # 更新匹配的行
    test_df.loc[matches, '拍賣類別'] = rule_category_id
    test_df.loc[matches, '拍賣類別名稱'] = rule_category_name
    
    # 打印进度
    if (index + 1) % 100 == 0 or (index + 1) == len(rules_df):
        print(f"Processed rule {index + 1}/{len(rules_df)}")

print("Rule matching completed.")

# 将更新后的test DataFrame保存到新的Excel文件
output_file_path = 'updated_test.xlsx'
test_df.to_excel(output_file_path, index=False)

print(f"Updated file saved to {output_file_path}")

end = time.perf_counter()
print('running time : %s s'%(end-start))
# 计算程序运行时长
