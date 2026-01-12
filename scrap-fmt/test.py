from DrissionPage import WebPage
from DrissionPage.common import Settings
# from DrissionPage import ChromiumOptions
import pandas

# path = '/usr/bin/microsoft-edge-stable'
# ChromiumOptions().set_browser_path(path).save()
# 以上，用于给drissionpage添加配置：
# 配置已保存到文件: [path]/DrissionPage/_configs/configs.ini
# 以后程序可自动从文件加载配置

Settings().set_language('zh_cn')
tab = WebPage().latest_tab
tab.get('https://www.fmz.com/robot/597675')

page = WebPage()










# with open('test.json') as file:
#     file.write(t.content)
    


