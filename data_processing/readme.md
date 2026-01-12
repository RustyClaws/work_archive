1- 用到的库： pandas   re  
	**time模块用于计算运行时间**    
    python版本：3.10.12

2- 优化方案：
	正则化匹配规则的文本
	对正则部分进行预编译
	用str.contains()替代apply，节省运存
	用str.contains()和_append()以提高运行速度

3- 文件结构：
	match.py
		- 用于处理文档的代码文件，如有需要可在里面修改输入输出的文件名称
	規則.xlsx
		- 存放规则的文件
	test.xlsx
		- 待处理数据的文件
	optimized.png
		- 截图，优化**后**花费时常，单位：秒
	time_record.png
		- 截图，优化**前**花费时常，单位：秒
	updated_test_new.xlsx 
		- 运行match.py后，输出的文件
