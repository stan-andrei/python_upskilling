from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class SecAss(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/andrei.stan/upskilling/upskilling/exercices/assessment2/part2/venv-upskilling/lib/python3.8/site-packages/selenium/webdriver/chromedriver")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_selenium_page(self):
        driver = self.driver
        driver.get('http://www.google.com/');
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('selenium python')
        search_box.submit()
        driver.find_element_by_partial_link_text("Selenium with Python — Selenium Python Bindings 2 ...").click()
        assert "Selenium with Python" in driver.title
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('locating elements')
        search_box.submit()
        assert "Search" in driver.title
        driver.find_element_by_partial_link_text("Locating").click()
        assert "Locating Elements" in driver.title

    def tearDown(self):
            self.driver.quit()
            print("Test Completed")

if __name__ == "__main__":
        unittest.main()