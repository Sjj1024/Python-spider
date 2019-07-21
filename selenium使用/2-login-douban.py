from selenium import webdriver
import time

# 创建一个driver客户端
driver = webdriver.Chrome()

# 使用driver发送请求
driver.get("https://www.douban.com/")

# 操作填入数据
time.sleep(2)
driver.find_element_by_class_name("account-tab-account").click()
time.sleep(2)
driver.find_element_by_id("username").send_keys("15670339118")
time.sleep(2)
driver.find_element_by_id("password").send_keys("521douban")

time.sleep(5)
# 截图保存
driver.save_screenshot("douban.png")

# 退出浏览器
driver.quit()