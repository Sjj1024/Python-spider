from selenium import webdriver
import time

# 创建一个driver客户端
driver = webdriver.Chrome()

# 使用driver发送请求
driver.get("http://www.renren.com/SysHome.do")

# 操作填入数据
time.sleep(2)
driver.find_element_by_id("email").send_keys("15670339118")
time.sleep(2)
driver.find_element_by_id("password").send_keys("15670339118")
time.sleep(2)
driver.find_element_by_id("login").click()
time.sleep(5)
# 截图保存
driver.save_screenshot("douban.png")

# 退出浏览器
driver.quit()