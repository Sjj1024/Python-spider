from selenium import webdriver

url = "https://movie.douban.com/chart"
driver = webdriver.Chrome()

driver.get(url)

res1 = driver.find_elements_by_xpath('//div[@class="pl2"]')

print(res1)

driver.quit()