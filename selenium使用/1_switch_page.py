import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

time.sleep(3)
news_obj = driver.find_element_by_id("jgwab").click()

print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

driver.save_screenshot("wang.png")



