import time
from selenium import webdriver


url = "https://movie.douban.com/chart"
driver = webdriver.Chrome()

driver.get(url)

time.sleep(2)
res1 = driver.find_elements_by_xpath('//div[@class="pl2"]/a')
print(res1)
print("*"*10)
for i in res1:
    # 获取到a标签，并打印a标签的text和链接
    print(i.text, i.get_attribute("href"))

driver.quit()