from selenium import webdriver


class Douban(object):
    def __init__(self):
        self.url = "https://movie.douban.com/chart"
        self.driver = webdriver.Chrome()

    def parse_title(self):
        self.driver.get(self.url)
        self.driver.find_elements_by_xpath("")

    def run(self):
        # 发送请求

        self.driver.get(self.url)

        # 解析数据
        self.parse_title()

        # 保存数据


if __name__ == '__main__':
    Douban().run()
