import unittest
from selenium import webdriver
from time import sleep

class MercadoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\erick\Downloads\chromedriver_win32\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://mercadolibre.com/")


    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        driver.execute_script("arguments[0].click();", order_menu)
        higher_price = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-view-options > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a > div > div')
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(3)


        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
            prices.append(article_price)
        print(articles, prices)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)