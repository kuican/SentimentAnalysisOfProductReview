from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import json

class review(object):
    def init(self):
        self.login_url = "https://login.tmall.com/?spm=a220o.1000855.a2226mz.2.7b6a493atgGt1e&redirectURL=https%3A%2F%2Fdetail.tmall.com%2Fitem.htm%3Fspm%3Da230r.1.14.1.78d33b3a4zmgeA%26id%3D602909085750%26ns%3D1%26abbucket%3D1%26sku_properties%3D10004%3A709990523%3B5919063%3A6536025"
        self.url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.9.76f96228yVEeeJ&id=602659642364&cm_id=140105335569ed55e27b&abbucket=1"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.9.76f96228yVEeeJ&id=602659642364&cm_id=140105335569ed55e27b&abbucket=1',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-mode': 'sec-fetch-mode',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        }

        self.drivername = "chrome"
        self.path = "/Users/chensx/Desktop/graduation_project/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def get_review(self):
        print("get")
        self.driver.find_element_by_css_selector("a[tabindex=\"-1\"][href=\"#J_Reviews\"]").click()
        num = 0
        while num < 20:
            sleep(3)
            self.driver.execute_script("window.scrollBy(0,1000)")
            i = 0
            while i < 4:
                self.driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
                i += 1
            review_list = self.driver.find_elements_by_class_name("tm-col-master")
            for review in review_list:
                text = str(review.find_element_by_class_name("tm-rate-fulltxt").text)
                with open("review.csv", 'a') as fp:
                    fp_csv = csv.writer(fp)
                    fp_csv.writerow([text])
                print(text)
            sleep(3)
            self.driver.find_element_by_link_text("下一页>>").click()
            num += 1

    def login(self):
        self.init()
        self.driver.get(url=self.login_url)
        input("请回车输入")
        self.dict_cookies = self.driver.get_cookies()
        self.json_cookies = json.dumps(self.dict_cookies)
        print(self.dict_cookies)
        self.get_review()



if __name__ == '__main__':
    get_review = review()
    get_review.login()
    get_review.driver.close()