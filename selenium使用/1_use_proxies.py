from selenium import webdriver
# 导入选项包
from selenium.webdriver.chrome.options import Options

# 创建chrome参数对象,设置chrome浏览器无界面模式
chrome_options=Options()
chrome_options.add_argument('--headless')
# 设置代理
chrome_options.add_argument("--proxy-server=http://202.20.16.82:10152")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152

# 创建chrome无界面对象
browser = webdriver.Chrome(options=chrome_options)

# 访问boss直聘
browser.get('https://www.zhipin.com/job_detail/?query=%E6%B5%8B%E8%AF%95&city=101010100&industry=&position=')

#打印内容
browser.save_screenshot("boss.png")
print(browser.page_source)