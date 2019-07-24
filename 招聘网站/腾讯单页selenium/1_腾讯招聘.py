from selenium import webdriver
import time
import os

# 实例化一个driver对象
driver = webdriver.Chrome()

# 调整浏览器大小
driver.set_window_size(1920, 1080)

# 模拟浏览器发送请求
driver.get("https://careers.tencent.com/search.html?query=ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006,ot_40001001")

time.sleep(5)
# 页面截图保存到本地
driver.save_screenshot("tengxun.png")

# 查看请求信息
html_source = driver.page_source
html_cookie = driver.get_cookies()
html_url = driver.current_url

# 保存到指定的文件夹中
with open("tengxun.html", "w", encoding="utf-8") as f:
    f.write(html_source)

# 关闭浏览器
driver.quit()