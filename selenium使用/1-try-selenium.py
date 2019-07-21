import shutil

from selenium import webdriver
import time
import os

# 实例化一个driver对象
driver = webdriver.Chrome()

# 调整浏览器大小
driver.set_window_size(1920, 1080)

# 模拟浏览器发送请求
driver.get("https://www.baidu.com/")

# 在input标签中输入内容
driver.find_element_by_id("kw").send_keys("美女")
driver.find_element_by_id("su").click()

time.sleep(5)
# 页面截图保存到本地
driver.save_screenshot("baidu.png")

# 查看请求信息
html_source = driver.page_source
html_cookie = driver.get_cookies()
html_url = driver.current_url

# print(html_source)
# 保存到指定的文件夹中
str_dir = "baidu"
os.mkdir(str_dir)
save_path = str_dir + "/" + "baidu.html"
with open(save_path, "w", encoding="utf-8") as f:
    f.write(html_source)

# 关闭浏览器
driver.quit()
