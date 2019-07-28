from selenium import webdriver
# 导入选项包
from selenium.webdriver.chrome.options import Options

# 创建chrome参数对象,设置chrome浏览器无界面模式
chrome_options=Options()
chrome_options.add_argument('--headless')

# 创建chrome无界面对象
browser = webdriver.Chrome(options=chrome_options)

# 访问boss直聘
browser.get('https://www.zhipin.com/job_detail/?query=%E6%B5%8B%E8%AF%95&city=101010100&industry=&position=')

#打印内容
browser.save_screenshot("boss.png")
print(browser.page_source)